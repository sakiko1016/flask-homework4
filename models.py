from flask_sqlalchemy import SQLAlchemy
from app import app
db = SQLAlchemy(app)

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(80), unique=True, nullable=False)
  password = db.Column(db.String(120), nullable=False)

  def __repr__(self):
    return f'<User {self.username}>'

class Car(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  make = db.Column(db.String(80), nullable=False)
  model = db.Column(db.String(120))
  year = db.Column(db.Integer)

  def __repr__(self):
    return f'<Car {self.make} {self.model}>'