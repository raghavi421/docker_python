# app.py
import os
import time
import psycopg2

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = int(os.getenv("DB_PORT", 5432))
DB_NAME = os.getenv("DB_NAME", "appdb")
DB_USER = os.getenv("DB_USER", "appuser")
DB_PASS = os.getenv("DB_PASS", "apppass")

print("connecting to postgresql")

# Retry loop to wait for DB to become ready
max_attempts = 10
for attempt in range(1, max_attempts + 1):
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            port=DB_PORT,
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASS,
        )
        break
    except Exception as e:
        print(f"Attempt {attempt}/{max_attempts} - DB not ready: {e}")
        if attempt == max_attempts:
            raise
        time.sleep(2)

print("connecting to database")
conn.autocommit = True
cur = conn.cursor()

# Create table if not exists
cur.execute("""
CREATE TABLE IF NOT EXISTS persons (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);
""")

print("data base rows")

# Insert one row
cur.execute("INSERT INTO persons (name) VALUES (%s) RETURNING id, name;", ("raghavi",))
inserted = cur.fetchone()
print("Inserted row:", inserted)

# Read back rows
cur.execute("SELECT id, name FROM persons;")
rows = cur.fetchall()

# Table printing
print("All rows in table format:")
print("+----+--------+")
print("| id | name   |")
print("+----+--------+")
for row in rows:
    print(f"| {row[0]:<2} | {row[1]:<6} |")
print("+----+--------+")

cur.close()
conn.close()

print("data base connection closed")
