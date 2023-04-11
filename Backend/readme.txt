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
        "role": "s",
        "surname": "Gulotta"
}

{
        "age": 55,
        "cf": "MNGBBR68D48A785Z",
        "emailAddress": "barbara.mingardi.studio@fitstic-edu.com",
        "id": 2,
        "name": "Barbara",
        "password": "Passw0rd!",
        "phoneNumber": 3343932783,
        "role": "s",
        "surname": "Mingardi"
}

{
        "age": 20,
        "cf": "GLTNDR02E16A785N",
        "emailAddress": "andrea.gulotta.studio@fitstic-edu.com",
        "id": 3,
        "name": "Andrea",
        "password": "Passw0rd!",
        "phoneNumber": 3703226229,
        "role": "t",
        "surname": "Gulotta"
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
    "price": 350,
    "subject": "Linguaggio Python",
    "teacherId": 4,
    "title": "Python"
}