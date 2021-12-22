from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from faker import Faker
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@192.168.233.138:5532/eshop'
db = SQLAlchemy(app)

class User(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(80), unique = True)
    email = db.Column(db.String(120), unique = True)
    create_time = db.Column(db.DateTime)

    def __init__(self, user):
        self.username = user['username']
        self.email = user['email']
        self.create_time = user['create_time']
    
    def __repr__(self):
        return '<User %r>' % self.username


if __name__ == '__main__':

    faker = Faker()

    # ------------------------INSERT DATA--------------------------------------------
    profile = faker.simple_profile()

    user = {
        'username': profile['username'],
        'email': profile['mail'],
        'create_time': datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
    }

    user = User(user)
    db.session.add(user)
    db.session.commit()

    # -----------------------QUERY DATA----------------------------------------------
    users = User.query.all()
    print('All users')
    print(users)

    print('Filter by id')
    users = User.query.filter_by(id = 2).all()
    print(user)

    print('Filter by specific create time')
    user = User.query.filter_by(create_time = '2021-12-21 23:40:26').first()
    print(user)
    
    print('Filter by a range of time')
    user = User.query.filter(User.create_time > '2021-12-21 23:40:26').all()
    print(user)