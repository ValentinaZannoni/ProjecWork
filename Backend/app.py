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
  return "user updated"

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

# Course get_all_byStudentId
@app.route('/courses/student/<studentId>', methods=['GET'])
def get_courses_byStudentId(studentId):
  courses = []
  for s in db.session.query(Students).all():
    del s.__dict__['_sa_instance_state']
    if int(studentId) in s.__dict__['idStudents']:
      idC = s.__dict__['idCourse']
      course = Course.query.get(idC)
      del course.__dict__['_sa_instance_state']
      courses.append(course.__dict__)
  return jsonify(courses)

# Course get_all_byStudentId not student
@app.route('/courses/not-student/<studentId>', methods=['GET'])
def get_courses_not_byStudentId(studentId):
  courses = []
  for s in db.session.query(Students).all():
    del s.__dict__['_sa_instance_state']
    if int(studentId) not in s.__dict__['idStudents']:
      idC = s.__dict__['idCourse']
      course = Course.query.get(idC)
      del course.__dict__['_sa_instance_state']
      courses.append(course.__dict__)
  return jsonify(courses)

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

# Course and Student create
@app.route('/courses-students', methods=['POST'])
def create_coursesStudents():
  body = request.get_json()
  db.session.add(Course(title=body['title'], description=body['description'], subject=body['subject'], price=body['price'], teacherId=body['teacherId']))
  db.session.commit()
  c = db.session.query(Course).order_by(Course.id.desc()).first()
  db.session.add(Students(idCourse = c.__dict__['id'], idStudents = []))
  db.session.commit()
  return "course and students created"

# Course and Student delete
@app.route('/courses-students/<id>', methods=['DELETE'])
def delete_coursesStudents(id):
  db.session.query(Course).filter_by(id=id).delete()
  db.session.commit()
  db.session.query(Students).filter_by(idCourse=id).delete()
  db.session.commit()
  return "course and students deleted"

# student get_all
@app.route('/students', methods=['GET'])
def get_students():
  students = []
  for s in db.session.query(Students).all():
    del s.__dict__['_sa_instance_state']
    students.append(s.__dict__)
  return jsonify(students)

# student get_single
@app.route('/students/<idCourse>', methods=['GET'])
def get_student(idCourse):
  student = Students.query.get(idCourse)
  del student.__dict__['_sa_instance_state']
  return jsonify(student.__dict__)

# student create
@app.route('/students', methods=['POST'])
def create_student():
  body = request.get_json()
  db.session.add(Students(idCourse=body['idCourse'], idStudents=body['idStudents']))
  db.session.commit()
  return "item created"

# student update
@app.route('/students/<idCourse>', methods=['PUT'])
def modify_student(idCourse):
  body = request.get_json()
  db.session.query(Students).filter_by(idCourse=idCourse).update(
    dict(idStudents = body['idStudents']))
  db.session.commit()
  return "student updated"

# student delete
@app.route('/students/<idCourse>', methods=['DELETE'])
def delete_student(idCourse):
  db.session.query(Students).filter_by(idCourse=idCourse).delete()
  db.session.commit()
  return "student deleted"