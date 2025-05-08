import psycopg2
import os

def get_db_conn():
    return psycopg2.connect(
        dbname = os.getenv("POSTGRES_DB", "geodb"),
        user = os.getenv("POSTGRES_USER", "geo"),
        password = os.getenv("POSTGRES_PASSWORD", "secret"),
        host = os.getenv("POSTGRES_HOST", "postgis"),
        port = os.getenv("POSTGRES_PORT", 5432)
    )

def save_location(payload):
    conn = get_db_conn()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO device_locations (device_id, location, timestamp)
            VALUES (%s, ST_SetSRID(ST_MakePoint(%s, %s), 4326), %s)
        """, (
            payload["device_id"],
            payload["lon"],
            payload["lat"],
            payload["timestamp"]
        ))
        conn.commit()
    except Exception as e:
        print("Error saving to DB:", e)
    finally:
        cursor.close()
        conn.close()