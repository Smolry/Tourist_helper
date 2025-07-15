const BASE_URL = "http://localhost:8000"; // Change if your backend URL is different

export async function planTour({ lat, lon, interest, limit }) {
  const res = await fetch(`${BASE_URL}/plan-tour`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ lat, lon, interest, limit })
  });

  if (!res.ok) {
    const error = await res.json();
    throw new Error(error.error || "API request failed");
  }

  return await res.json();
}
