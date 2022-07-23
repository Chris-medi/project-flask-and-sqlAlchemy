from database.database import db
from werkzeug.security import generate_password_hash, check_password_hash

class UsersModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(),unique=True, nullable=False)
    email = db.Column(db.String())
    password = db.Column(db.String(),unique=True, nullable=False)


    def __init__ (self,name,email,password):

        self.password = generate_password_hash(password)
        self.name = name
        self.email = email


    def verify_password(self, pwd):
        return check_password_hash(self.password, pwd)