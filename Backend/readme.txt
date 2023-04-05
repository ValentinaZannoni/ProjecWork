docker compose up -d db
docker compose up -d --build pythonapp
docker exec -it db psql -U postgres
Con postman fare le richieste all'indirizzo http://localhost:80/

{
        "name": "Federico",
        "surname": "Gulotta",
        "phoneNumber": 3664294909,
        "emailAddress": "federico.gulotta.studio@fitstic-edu.com",
        "password": "Passw0rd!",
        "age": 23,
        "role": "s",
        "cf": "GLTFRC00A08A785K"
}

{
        "title": "Corso",
        "subject": "Materia",
        "description": "Descrizione",
        "idTeacher": 1,
        "price": 100
}