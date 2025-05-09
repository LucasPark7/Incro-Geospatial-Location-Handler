from kafka import KafkaProducer, errors
import json
import os

def get_producer():
    kafka_host = os.getenv("KAFKA_HOST", "kafka.default.svc.cluster.local:9092")
    try:
        producer = KafkaProducer(
            bootstrap_servers=kafka_host,
            value_serializer=lambda v: json.dumps(v).encode("utf-8")
        )
        return producer
    except errors.NoBrokersAvailable:
        print(f"Kafka broker not available at {kafka_host}")
        raise