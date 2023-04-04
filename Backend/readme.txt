docker compose up -d db
docker compose up -d --build pythonapp
docker exec -it db psql -U postgres
Con postman fare le richieste all'indirizzo http://localhost:80/


{
	"name":"Luca",
    "surname":"Bottoni",
    "phoneNumber": 345608413,
    "emailAddress": "luca.bottoni.studio@fitstic-edu.com",
    "password": "Passw0rd!",
    "age": 20,
    "role": "t",
    "cf": "BTTLCU02P22C573H"
}

{
	"title":"Gabriele Dannunzio",
    "subject":"Italiano",
    "description": "In questo corso si parlera dellla storia dello scrittore Gabriele DAnnunzio e delle sue scrittore",
    "idTeacher": 1,
    "price": 450
}