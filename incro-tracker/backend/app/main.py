from fastapi import FastAPI, HTTPException
from .db import save_location

app = FastAPI()

@app.post("/location")
async def receive_location(payload: dict):
    required = {"device_id", "lat", "lon", "timestamp"}
    if not required.issubset(payload):
        raise HTTPException(status_code=400, detail="Missing required fields")

    # store in PostGIS
    save_location(payload)

    return {"status": "received"}