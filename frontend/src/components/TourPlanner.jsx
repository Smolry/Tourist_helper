import { useState } from "react";
import { planTour } from "../api";
import PlaceCard from "./PlaceCard";

export default function TourPlanner() {
  const [lat, setLat] = useState("");
  const [lon, setLon] = useState("");
  const [interest, setInterest] = useState("tourist attractions");
  const [limit, setLimit] = useState(5);
  const [tour, setTour] = useState([]);
  const [loading, setLoading] = useState(false);

  const handlePlanTour = async () => {
    setLoading(true);
    try {
      const res = await planTour({ lat: parseFloat(lat), lon: parseFloat(lon), interest, limit });
      setTour(res.tour || []);
    } catch (e) {
      alert("Failed to plan tour: " + e.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="max-w-3xl mx-auto">
      <div className="bg-white shadow-lg rounded-lg p-6 mb-6">
        <div className="grid grid-cols-2 gap-4">
          <input
            className="border border-gray-300 p-2 rounded focus:outline-none focus:ring-2 focus:ring-blue-400"
            placeholder="Latitude"
            value={lat}
            onChange={(e) => setLat(e.target.value)}
          />
          <input
            className="border border-gray-300 p-2 rounded focus:outline-none focus:ring-2 focus:ring-blue-400"
            placeholder="Longitude"
            value={lon}
            onChange={(e) => setLon(e.target.value)}
          />
          <input
            className="col-span-2 border border-gray-300 p-2 rounded focus:outline-none focus:ring-2 focus:ring-blue-400"
            placeholder="Interest (e.g. museums)"
            value={interest}
            onChange={(e) => setInterest(e.target.value)}
          />
          <input
            type="number"
            min={1}
            max={10}
            className="border border-gray-300 p-2 rounded focus:outline-none focus:ring-2 focus:ring-blue-400"
            value={limit}
            onChange={(e) => setLimit(Number(e.target.value))}
          />
          <button
            className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 transition"
            onClick={handlePlanTour}
            disabled={loading}
          >
            {loading ? "Planning..." : "Plan My Tour"}
          </button>
        </div>
      </div>

      <div>
        {tour.map((place) => (
          <PlaceCard key={place.fsq_id} place={place} />
        ))}
      </div>

      {tour.length > 0 && (
        <div className="text-center mt-6">
          <a
            href={`https://www.google.com/maps/dir/${tour.map(p => `${p.lat},${p.lon}`).join("/")}`}
            target="_blank"
            rel="noreferrer"
            className="inline-block bg-green-600 text-white px-6 py-2 rounded-lg shadow hover:bg-green-700 transition"
          >
            View Full Tour on Google Maps 🗺️
          </a>
        </div>
      )}
    </div>
  );
}