import datetime
from flask_login import UserMixin

from werkzeug.security import generate_password_hash, check_password_hash

from . import db

class User(db.Model, UserMixin):

  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key = True)
  username = db.Column(db.String(50), unique = True, nullable = False)
  encrypted_password = db.Column(db.String(100), nullable = False)
  email = db.Column(db.String(100), unique=True, nullable = False)
  created_at = db.Column(db.DateTime, default = datetime.datetime.now())

  def verify_password(self, password):
    return check_password_hash(self.encrypted_password, password)

  @property
  def password(self):
    pass

  @password.setter
  def password(self, value):
    self.encrypted_password = generate_password_hash(value)


  def __str__(self):
    return self.username

  @classmethod
  def createElement(cls, username, password, email):
    user = User(username=username, password=password, email=email)

    db.session.add(user)
    db.session.commit()

    return user

  @classmethod
  def get_by_username(cls, username):
    return User.query.filter_by(username=username).first()

  @classmethod
  def get_by_email(cls, email):
    return User.query.filter_by(email=email).first()

  @classmethod
  def get_by_id(cls, id):
    return User.query.filter_by(id=id).first()

  @classmethod
  def is_active(self):
    return self.is_active









