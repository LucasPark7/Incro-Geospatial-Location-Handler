export async function fetchLocations() {
    const res = await fetch('/api/locations'); // Adjust for backend route or proxy
    if (!res.ok) throw new Error("Failed to fetch data");
    return res.json();
  }  