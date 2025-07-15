import TourPlanner from "./components/TourPlanner";

export default function App() {
  return (
    <div className="min-h-screen bg-gray-50 p-6">
      <h1 className="text-4xl font-extrabold text-blue-700 text-center mb-6 drop-shadow-sm">
        ExploreAI 🧭
      </h1>
      <p className="text-center text-gray-600 mb-6 max-w-xl mx-auto">
        Personalized tours powered by Foursquare and AI. Enter your location & interests to discover amazing places.
        <div className="bg-green-500 text-white p-4 rounded">Tailwind is working 🎉</div>

      </p>
      <TourPlanner />
    </div>
  );
}