from enum import unique

from sqlalchemy.orm import backref
from . import login_manager
from datetime import datetime
from flask_login import UserMixin
from . import db
from werkzeug.security import generate_password_hash,check_password_hash


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80))
    email = db.Column(db.string(50), unique=True)
    hash_pass = db.Column(db.String(255))
    comments = db.relationship('Comment', backref = 'user', lazy = 'dynamic')
    blogs = db.relationship('Blog', backref = 'user', lazy = 'dynamic')
    profile_pic_path = db.Column(db.String())
    bio = db.Column(db.String(255))


    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, pass_entry):
        self.hash_pass = generate_password_hash(pass_entry)

    def verify_pasword(self, pass_entry):
        return check_password_hash(self.hash_pass, pass_entry)

    def save(self):
        db.session.add(self)
        db.session.commit()
        return self.id

    def __repr__(self):
        return f'User {self.username}::{self.id}'

class Blog(db.Model):
    __tablename__ = 'blogs'

    id = db.Column