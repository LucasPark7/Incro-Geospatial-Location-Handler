import React, { useEffect, useState } from 'react';
import MapView from './MapView';
import { fetchLocations } from './api';

export default function App() {
  const [locations, setLocations] = useState([]);

  useEffect(() => {
    const loadData = async () => {
      try {
        const data = await fetchLocations();
        setLocations(data);
      } catch (err) {
        console.error('Failed to fetch locations:', err);
      }
    };

    loadData();
    const interval = setInterval(loadData, 5000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div>
      <MapView devices={locations} />
    </div>
  );
}