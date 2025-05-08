from kafka import KafkaProducer
import json
import os

def get_producer():
    kafka_host = os.getenv("KAFKA_HOST", "my-cluster-kafka-bootstrap.kafka:9092")
    return KafkaProducer(
        bootstrap_servers=kafka_host,
        value_serializer=lambda v: json.dumps(v).encode("utf-8")
    )