docker compose up -d db
docker compose up -d --build pythonapp
docker exec -it db psql -U postgres
Con postman fare le richieste all'indirizzo http://localhost:80/


{
	"name":"Luca",
    "surname":"Bottoni",
    "phoneNumber": 3456084130,
    "emailAddress": "luca.bottoni.studio@fitstic-edu.com",
    "password": "Passw0rd!",
    "age": 20,
    "role": "t",
    "cf": "BTTLCU02P22C573H"
}
{
    "description": "Montale e i suoi romanzi",
    "price": 350,
    "subject": "Letteratura",
    "teacherId": 1,
    "title": "Montale"
}