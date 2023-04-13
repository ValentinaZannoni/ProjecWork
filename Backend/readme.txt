docker compose up -d db
docker compose up -d --build pythonapp
docker exec -it db psql -U postgres
Con postman fare le richieste all'indirizzo http://localhost:80/

#Users
    {
        "age": 23,
        "cf": "GLTFRC00A08A785K",
        "emailAddress": "federico.gulotta.studio@fitstic-edu.com",
        "id": 1,
        "name": "Federico",
        "password": "Passw0rd!",
        "phoneNumber": 3664294909,
        "role": "S",
        "surname": "Gulotta"
    },
    {
        "age": 23,
        "cf": "BTTLCU00A08A785K",
        "emailAddress": "luca.bottoni.studio@fitstic-edu.com",
        "id": 2,
        "name": "Luca",
        "password": "Passw0rd!",
        "phoneNumber": 3456084130,
        "role": "S",
        "surname": "Bottoni"
    },
    {
        "age": 23,
        "cf": "VLNZNN00A08A785K",
        "emailAddress": "valentina.zannoni.studio@fitstic-edu.com",
        "id": 3,
        "name": "Valentina",
        "password": "Passw0rd!",
        "phoneNumber": 3337739329,
        "role": "S",
        "surname": "Zannoni"
    },
    {
        "age": 23,
        "cf": "LSSDTL00A08A785K",
        "emailAddress": "alessandro.dastolfo.studio@fitstic-edu.com",
        "id": 4,
        "name": "Alessandro",
        "password": "Passw0rd!",
        "phoneNumber": 3339239744,
        "role": "T",
        "surname": "D'astolfo"
    },
    {
        "age": 23,
        "cf": "LRRGVN00A08A785K",
        "emailAddress": "lorraine.garavini.studio@fitstic-edu.com",
        "id": 5,
        "name": "Lorraine",
        "password": "Passw0rd!",
        "phoneNumber": 3426608612,
        "role": "T",
        "surname": "Garavini"
    }

#Courses
{
        "title": "SQL",
        "description": "Corso sui database e il linguaggio SQL",
        "subject": "Database SQL",
        "price": 200,
        "teacherId": 4
}

{
    "description": "Corso sul linguaggio di programmazione C#",
    "id": 2,
    "price": 300,
    "subject": "Linguaggio C#",
    "teacherId": 4,
    "title": "C#"
}

{
    "description": "Corso sul linguaggio di programmazione Python",
    "id": 3,
    "price": 400,
    "subject": "Linguaggio Python",
    "teacherId": 5,
    "title": "Python"
}

{
    "description": "Corso sul linguaggio di programmazione Java",
    "id": 3,
    "price": 500,
    "subject": "Linguaggio Java",
    "teacherId": 5,
    "title": "Java"
}