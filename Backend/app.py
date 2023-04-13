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

class Classmates(db.Model):
  idCourse = db.Column(db.Integer, primary_key=True)
  idStudents = db.Column(db.ARRAY(db.Integer), default=[])

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
  return {
          "response": "user created"
        }

# User update
@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
  body = request.get_json()
  db.session.query(User).filter_by(id=id).update(
    dict(name=body['name'], surname=body['surname'], phoneNumber=body['phoneNumber'], emailAddress=body['emailAddress'], password=body['password'], age=body['age'], role=body['role'], cf=body['cf']))
  db.session.commit()
  return {
          "response": "user modified"
        }

# User delete
@app.route('/users/delete/<email>', methods=['DELETE'])
def delete_user(email):
  db.session.query(User).filter_by(emailAddress=email).delete()
  db.session.commit()
  return {
          "response": "User deleted"
        }

# Course get_all
@app.route('/courses', methods=['GET'])
def get_courses():
  courses = []
  for item in db.session.query(Course).all():
    del item.__dict__['_sa_instance_state']
    courses.append(item.__dict__)
  return jsonify(courses)

# Course get_all_byTeacherId
@app.route('/courses/teacher/<teacherId>', methods=['GET'])
def get_courses_byTeacherId(teacherId):
  courses = []
  for course in db.session.query(Course).filter_by(teacherId = teacherId):
    del course.__dict__['_sa_instance_state'] 
    courses.append(course.__dict__)
  return jsonify(courses)

# Course get_all_subscribed
@app.route('/courses/subscribed/<studentId>', methods=['GET'])
def get_all_subscribed(studentId):
  courses = []
  for s in db.session.query(Classmates).all():
    del s.__dict__['_sa_instance_state']
    if int(studentId) in s.__dict__['idStudents']:
      idC = s.__dict__['idCourse']
      course = Course.query.get(idC)
      del course.__dict__['_sa_instance_state']
      courses.append(course.__dict__)
  return jsonify(courses)

# Course get_all_not_subscribed
@app.route('/courses/not_subscribed/<studentId>', methods=['GET'])
def get_all_not_subscribed(studentId):
  courses = []
  for s in db.session.query(Classmates).all():
    del s.__dict__['_sa_instance_state']
    if int(studentId) not in s.__dict__['idStudents']:
      idC = s.__dict__['idCourse']
      course = Course.query.get(idC)
      del course.__dict__['_sa_instance_state']
      courses.append(course.__dict__)
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
        return {
          "response": "User exist"
        }
  else:
        return {
          "response": "User does not exist"
        }

# Course and classmates create
@app.route('/courses-classmates', methods=['POST'])
def create_courses_classmates():
  body = request.get_json()
  db.session.add(Course(title=body['title'], description=body['description'], subject=body['subject'], price=body['price'], teacherId=body['teacherId']))
  db.session.commit()
  c = db.session.query(Course).order_by(Course.id.desc()).first()
  db.session.add(Classmates(idCourse = c.__dict__['id'], idStudents = []))
  db.session.commit()
  return "course and classmates created"

# Course and classmates delete
@app.route('/courses-classmates/<id>', methods=['DELETE'])
def delete_courses_classmates(id):
  db.session.query(Course).filter_by(id=id).delete()
  db.session.commit()
  db.session.query(Classmates).filter_by(idCourse=id).delete()
  db.session.commit()
  return "course and classmates deleted"

# classmates get_all
@app.route('/classmates', methods=['GET'])
def get_classmates():
  classmates = []
  for s in db.session.query(Classmates).all():
    del s.__dict__['_sa_instance_state']
    classmates.append(s.__dict__)
  return jsonify(classmates)

# classmates get_single
@app.route('/classmates/<idCourse>', methods=['GET'])
def get_student(idCourse):
  classmates = Classmates.query.get(idCourse)
  del classmates.__dict__['_sa_instance_state']
  return jsonify(classmates.__dict__)

# classmates create
@app.route('/classmates', methods=['POST'])
def create_classmates():
  body = request.get_json()
  db.session.add(Classmates(idCourse=body['idCourse'], idStudents=body['idStudents']))
  db.session.commit()
  return "item created"

# classmates update
@app.route('/classmates/<idCourse>', methods=['PUT'])
def update_classmates(idCourse):
  body = request.get_json()
  db.session.query(Classmates).filter_by(idCourse=idCourse).update(
    dict(idStudents = body['idStudents']))
  db.session.commit()
  return "classmates updated"

# classmates delete
@app.route('/classmates/<idCourse>', methods=['DELETE'])
def delete_classmates(idCourse):
  db.session.query(Classmates).filter_by(idCourse=idCourse).delete()
  db.session.commit()
  return "classmates deleted"