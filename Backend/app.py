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

# User get_all
@app.route('/users', methods=['GET'])
def get_users():
  users = []
  for user in db.session.query(User).all():
    del user.__dict__['_sa_instance_state']
    users.append(user.__dict__)
  return jsonify(users)

# User get_single
@app.route('/users/<id>', methods=['GET'])
def get_user(id):
  user = User.query.get(id)
  del user.__dict__['_sa_instance_state']
  return jsonify(user.__dict__)

# User get_single_byMail
@app.route('/users/mail/<email>', methods=['GET'])
def get_user_byMail(email):
  user = db.session.query(User).filter_by(emailAddress=email).first()
  del user.__dict__['_sa_instance_state']
  return jsonify(user.__dict__)

# User create
@app.route('/users', methods=['POST'])
def create_user():
  body = request.get_json()
  db.session.add(User(name=body['name'], surname=body['surname'], phoneNumber=body['phoneNumber'], emailAddress=body['emailAddress'], password=body['password'], age=body['age'], role=body['role'], cf=body['cf']))
  db.session.commit()
  return "user created"

# User update
@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
  body = request.get_json()
  db.session.query(User).filter_by(id=id).update(
    dict(name=body['name'], surname=body['surname'], phoneNumber=body['phoneNumber'], emailAddress=body['emailAddress'], password=body['password'], age=body['age'], role=body['role'], cf=body['cf']))
  db.session.commit()
  return 0

# User delete
@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
  db.session.query(User).filter_by(id=id).delete()
  db.session.commit()
  return "user deleted"

# Course get_all
@app.route('/courses', methods=['GET'])
def get_courses():
  courses = []
  for item in db.session.query(Course).all():
    del item.__dict__['_sa_instance_state']
    courses.append(item.__dict__)
  return jsonify(courses)

# Course get_single
@app.route('/courses/<id>', methods=['GET'])
def get_course(id):
  course = Course.query.get(id)
  del course.__dict__['_sa_instance_state']
  return jsonify(course.__dict__)

# Course create
@app.route('/courses', methods=['POST'])
def create_courses():
  body = request.get_json()
  db.session.add(Course(title=body['title'], description=body['description'], subject=body['subject'], price=body['price'], teacherId=body['teacherId']))
  db.session.commit()
  return "course created"

# Course update
@app.route('/courses/<id>', methods=['PUT'])
def update_course(id):
  body = request.get_json()
  db.session.query(Course).filter_by(id=id).update(
    dict(title=body['title'], description=body['description'], subject=body['subject'], price=body['price'], teacherId=body['teacherId']))
  db.session.commit()
  return "course updated"

# Course delete
@app.route('/courses/<id>', methods=['DELETE'])
def delete_course(id):
  db.session.query(Course).filter_by(id=id).delete()
  db.session.commit()
  return "course deleted"

# Authenticate
@app.route('/auth/<emailAddress>/<password>', methods=['GET'])
def check_password(emailAddress, password):
  user = User.query.filter_by(emailAddress=emailAddress, password=password).first()
  if user:
        return 'User exists in the database!'
  else:
        return 'User does not exist in the database.'
