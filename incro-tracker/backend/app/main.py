from fastapi import FastAPI, HTTPException
from kafka_producer import get_producer
from db import save_location

app = FastAPI()
producer = get_producer()

@app.post("/location")
async def receive_location(payload: dict):
    required = {"device_id", "lat", "lon", "timestamp"}
    if not required.issubset(payload):
        raise HTTPException(status_code=400, detail="Missing required fields")

    # push to Kafka
    producer.send("locations", payload)

    # store in PostGIS
    save_location(payload)

    return {"status": "received"}