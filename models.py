from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class StudentModel(db.Model):
	__tablename__ = 'students'
	id = db.Column(db.Integer, primary_key=True)
	firstname = db.Column(db.String(80))
	lastname = db.Column(db.String(80))
	email = db.Column(db.String(120))
	password = db.Column(db.String(120))
	gender = db.Column(db.String(80))
	hobbies = db.Column(db.String(120))
	country  = db.Column(db.String(120))
 
	def __init__(self,firstname, lastname, email, password, gender, hobbies, country):
		self.firstname = firstname
		self.lastname = lastname
		self.email = email
		self.password = password
		self.gender = gender
		self.hobbies = hobbies
		self.country = country
  
	def __repr__(self):
		return f"{self.firstname}:{self.lastname}"