from kafka import KafkaProducer, errors
import json
import os
import time

def get_producer():
    kafka_host = os.getenv("KAFKA_HOST", "kafka.default.svc.cluster.local:9092")
    for _ in range(10):
        try:
            producer = KafkaProducer(
                bootstrap_servers=['localhost:9092'],
                api_version=(2, 6, 0)
                #value_serializer=lambda v: json.dumps(v).encode("utf-8")
            )
            return producer
        except errors.NoBrokersAvailable:
            print(f"Kafka broker not available at {kafka_host}")
            time.sleep(5)
    raise Exception("Kafka broker not available")