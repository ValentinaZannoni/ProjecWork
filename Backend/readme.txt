docker compose up -d db
docker compose up -d --build pythonapp
docker exec -it db psql -U postgres
Con postman fare le richieste all'indirizzo http://localhost:80/