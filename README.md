# Python PostgreSQL Docker Application

This project demonstrates how to:
- Connect a Python application to PostgreSQL
- Automatically create a table
- Insert a row into the database
- Retrieve and display the row in table format
- Dockerize both the application and PostgreSQL
- Run them using a custom Docker network

## Features
| Component | Technology |
|----------|-------------|
| Backend  | Python |
| Database | PostgreSQL |
| Container Runtime | Docker |

## Project Structure
├── app.py
├── requirements.txt
├── Dockerfile
└── README.md
## create docker network
docker network create mynetwork
## Run Postgres container on the network
docker run -d \
  --name pg \
  --network mynetwork \
  -e POSTGRES_USER=appuser \
  -e POSTGRES_PASSWORD=apppass \
  -e POSTGRES_DB=appdb \
  -v pgdata:/var/lib/postgresql/data \
  postgres:15
## Build Python App Image
docker build -t app.py .
## Run the docker container
docker run --rm --name app.py --network mynetwork   -e DB_HOST=pg -e DB_PORT=5432 -e DB_NAME=appdb -e DB_USER=appuser -e DB_PASS=apppass   app.py
## Output
connecting to postgresql
connecting to database
data base rows
Inserted row: (9, 'raghavi')
All rows in table format:
+----+--------+
| id | name   |
+----+--------+
| 1  | Alice  |
| 2  | Alice  |
| 3  | Alice  |
| 4  | Alice  |
| 5  | Alice  |
| 6  | Alice  |
| 7  | Alice  |
| 8  | raghavi |
| 9  | raghavi |
+----+--------+
data base connection closed
## Push Image to Docker Hub
docker tag app.py praghavi123/app.py:latest
docker push praghavi123/app.py:latest
