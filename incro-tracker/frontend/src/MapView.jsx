import React from 'react';
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';
import L from 'leaflet';

const defaultIcon = new L.Icon({
  iconUrl: 'https://unpkg.com/leaflet@1.9.4/dist/images/marker-icon.png',
  iconSize: [25, 41],
  iconAnchor: [12, 41],
});

export default function MapView({ devices }) {
  const center = [40.7128, -74.0060]; // Default: New York City

  return (
    <MapContainer center={center} zoom={12} style={{ height: "100vh", width: "100%" }}>
      <TileLayer
        url='https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'
        attribution='© OpenStreetMap contributors'
      />
      {devices.map((device) => (
        <Marker
          key={device.device_id}
          position={[device.lat, device.lon]}
          icon={defaultIcon}
        >
          <Popup>
            <strong>ID:</strong> {device.device_id}<br />
            <strong>Time:</strong> {new Date(device.timestamp).toLocaleString()}
          </Popup>
        </Marker>
      ))}
    </MapContainer>
  );
}