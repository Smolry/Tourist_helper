export default function PlaceCard({ place }) {
  return (
    <div className="bg-white shadow-sm border border-gray-200 rounded p-4 mb-4 hover:shadow-md transition-shadow">
      <h2 className="text-xl font-semibold text-blue-700">{place.name}</h2>
      <p className="text-gray-600">{place.address}</p>
      <p className="text-sm text-gray-400">Distance: {place.distance}m</p>
      <a
        href={`https://www.google.com/maps?q=${place.lat},${place.lon}`}
        target="_blank"
        rel="noreferrer"
        className="text-sm text-blue-500 underline mt-2 inline-block"
      >
        📍 View on Google Maps
      </a>
    </div>
  );
}