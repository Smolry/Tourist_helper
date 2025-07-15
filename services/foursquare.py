import os
from dotenv import load_dotenv
import requests

load_dotenv()
FSQ_API_KEY = os.getenv("FSQ_KEY")


def search_places(
    lat: float,
    lon: float,
    query: str = "tourist attractions",
    limit: int = 5,
    radius: int = 5000
):
    url = "https://places-api.foursquare.com/places/search"
    headers = {
        "accept": "application/json",
        "authorization": f"Bearer {FSQ_API_KEY}",
        "X-Places-Api-Version": "2025-06-17"
    }
    params = {
        "ll": f"{lat},{lon}",
        "query": query,
        "limit": limit,
        "radius": radius,
        "open_now": True
    }

    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        raise Exception(
            f"Foursquare API error: {response.status_code} - {response.text}"
        )

    return response.json().get("results", [])


def get_place_details(fsq_id: str):
    url = f"https://places-api.foursquare.com/places/{fsq_id}"
    headers = {
        "accept": "application/json",
        "authorization": f"Bearer {FSQ_API_KEY}",
        "X-Places-Api-Version": "2025-06-17"
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Error fetching place details: {response.text}")
    
    return response.json()



def get_place_photo(fsq_id: str):
    url = f"https://places-api.foursquare.com/places/{fsq_id}/photos"
    headers = {
        "accept": "application/json",
        "authorization": f"Bearer {FSQ_API_KEY}",
        "X-Places-Api-Version": "2025-06-17"
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return None

    data = response.json()
    if data:
        photo = data[0]
        prefix = photo.get("prefix", "")
        suffix = photo.get("suffix", "")
        return f"{prefix}original{suffix}"
    return None

