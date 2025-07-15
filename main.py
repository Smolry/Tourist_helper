from fastapi import FastAPI, Query, Path
from services.foursquare import search_places, get_place_details
from pydantic import BaseModel
from typing import List
from services.foursquare import get_place_photo
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="ExploreAI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://tourist-helper.vercel.app"],  # Your frontend's domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/explore")
def explore(
    lat: float = Query(..., description="Latitude"),
    lon: float = Query(..., description="Longitude"),
    interest: str = Query("tourist attractions"),
    limit: int = Query(5, ge=1, le=10)
):
    """
    Return a personalized list of nearby places.
    """
    try:
        places = search_places(lat, lon, query=interest, limit=limit)
        return {"places": places}
    except Exception as e:
        return {"error": str(e)}


@app.get("/place/{fsq_id}")
def place_details(fsq_id: str = Path(..., description="Foursquare Place ID")):
    """
    Get detailed information about a specific place by fsq_id.
    """
    try:
        return get_place_details(fsq_id)
    except Exception as e:
        return {"error": str(e)}



class TourRequest(BaseModel):
    lat: float
    lon: float
    interest: str = "tourist attractions"
    limit: int = 5



@app.post("/plan-tour")
def plan_tour(request: TourRequest):
    """
    Plan a simple linear tour based on interest, location, and number of stops.
    """
    try:
        places = search_places(
            lat=request.lat,
            lon=request.lon,
            query=request.interest,
            limit=request.limit
        )

        # Sort by distance from the start point
        sorted_places = sorted(places, key=lambda p: p.get("distance", 999999))

        # Basic formatting
        itinerary = []
        for p in sorted_places:
            try:
                itinerary.append({
                    "name": p.get("name", "Unknown"),
                    "address": p.get("location", {}).get("formatted_address", "Unknown"),
                    "fsq_id": p.get("fsq_id", ""),
                    "lat": p.get("geocodes", {}).get("main", {}).get("latitude"),
                    "lon": p.get("geocodes", {}).get("main", {}).get("longitude"),
                    "distance": p.get("distance", "?"),
                    "photo": get_place_photo(p.get("fsq_id", ""))

                })
            except Exception as e:
                print(f"Skipping place due to error: {e}")
        # Google Maps Directions URL
        waypoints = "/".join(
             [f'{p["lat"]},{p["lon"]}' for p in itinerary if p["lat"] and p["lon"]])
        maps_url = f"https://www.google.com/maps/dir/{waypoints}"


        return {"tour": itinerary,
                "maps_url": maps_url
                }
    except Exception as e:
        return {"error": str(e)}

