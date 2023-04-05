from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

import os

app = Flask(__name__)
CORS(app)

if __name__ == '__main__':
    app.run(debug=True)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
db = SQLAlchemy(app)

class Item(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  titolo = db.Column(db.String(80), unique=True, nullable=False)
  regista = db.Column(db.String(80), unique=True, nullable=False)
  compagnia = db.Column(db.String(80), unique=True, nullable=False)

  def __init__(self, titolo, regista, compagnia):
    self.titolo = titolo
    self.regista = regista
    self.compagnia = compagnia

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(80), nullable=False)
  surname = db.Column(db.String(80), nullable=False)
  phoneNumber = db.Column(db.BigInteger, unique=True, nullable=False)
  emailAddress = db.Column(db.String(80), unique=True, nullable=False)
  password = db.Column(db.String(80),  nullable=False)
  age = db.Column(db.Integer,  nullable=False)
  role = db.Column(db.String(80),  nullable=False)
  cf = db.Column(db.String(80), unique=True, nullable=False)

  def __init__(self, name, surname, phoneNumber, emailAddress, password, age, role, cf):
    self.name = name
    self.surname = surname
    self.phoneNumber = phoneNumber
    self.emailAddress = emailAddress
    self.password = password
    self.age = age
    self.role = role
    self.cf = cf

class Course(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(80), unique=True, nullable=False)
  subject =  db.Column(db.String(80), unique=True, nullable=False)
  description = db.Column(db.String(150), nullable=False)
  teacherId = db.Column(db.Integer, nullable=False)
  price = db.Column(db.Integer, nullable=False)

  def __init__(self, title, subject, description, teacherId, price):
    self.title = title
    self.subject = subject
    self.description = description
    self.teacherId = teacherId
    self.price = price

class Students(db.Model):
  idCourse = db.Column(db.Integer, primary_key=True)
  idStudents = db.Column(db.Integer)

  def __init__(self, idCourse, idStudents):
    self.idCourse = idCourse
    self.idStudents = idStudents

db.create_all()

# User
@app.route('/users/<id>', methods=['GET'])
def get_user(id):
  user = User.query.get(id)
  del user.__dict__['_sa_instance_state']
  return jsonify(user.__dict__)

@app.route('/users', methods=['GET'])
def get_users():
  users = []
  for user in db.session.query(User).all():
    del user.__dict__['_sa_instance_state']
    users.append(user.__dict__)
  return jsonify(users)

@app.route('/users', methods=['POST'])
def create_user():
  body = request.get_json()
  db.session.add(User(name=body['name'], surname=body['surname'], phoneNumber=body['phoneNumber'], emailAddress=body['emailAddress'], password=body['password'], age=body['age'], role=body['role'], cf=body['cf']))
  db.session.commit()
  return "user created"

# Course
@app.route('/courses', methods=['POST'])
def create_courses():
  body = request.get_json()
  db.session.add(Course(title=body['title'], description=body['description'], subject=body['subject'], price=body['price'], teacherId=body['teacherId']))
  db.session.commit()
  return "course created"

@app.route('/courses/<id>', methods=['GET'])
def get_course(id):
  course = Course.query.get(id)
  del course.__dict__['_sa_instance_state']
  return jsonify(course.__dict__)

@app.route('/courses', methods=['GET'])
def get_courses():
  courses = []
  for item in db.session.query(Course).all():
    del item.__dict__['_sa_instance_state']
    courses.append(item.__dict__)
  return jsonify(courses)

# item
@app.route('/items/<id>', methods=['GET'])
def get_item(id):
  item = Item.query.get(id)
  del item.__dict__['_sa_instance_state']
  return jsonify(item.__dict__)

@app.route('/items', methods=['GET'])
def get_items():
  items = []
  for item in db.session.query(Item).all():
    del item.__dict__['_sa_instance_state']
    items.append(item.__dict__)
  return jsonify(items)

@app.route('/items', methods=['POST'])
def create_item():
  body = request.get_json()
  db.session.add(Item(body['titolo'], body['regista'], body['compagnia']))
  db.session.commit()
  return "item created"

@app.route('/items/<id>', methods=['PUT'])
def update_item(id):
  body = request.get_json()
  db.session.query(Item).filter_by(id=id).update(
    dict(titolo=body['titolo'], regista=body['regista'], compagnia=body['compagnia']))
  db.session.commit()
  return "item updated"

@app.route('/items/<id>', methods=['DELETE'])
def delete_item(id):
  db.session.query(Item).filter_by(id=id).delete()
  db.session.commit()
  return "item deleted"