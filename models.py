from extensions import db, login_manager
from flask_login import UserMixin
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(20), unique=True, nullable=False)

    email = db.Column(db.String(150), unique=True, nullable=False)

    phone = db.Column(db.String(20), unique=True, nullable=False)
    
    password_hash = db.Column(db.String(200), nullable=False)

    expenses = db.relationship('Expense', backref='owner', lazy=True)

    budgets = db.relationship('Budget', backref='owner', lazy=True)


class Expense(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    category = db.Column(db.String(100), nullable=False)

    amount = db.Column(db.Float, nullable=False)

    description = db.Column(db.Text)

    payment_method = db.Column(db.String(100))

    date = db.Column(db.DateTime, default=datetime.utcnow)
    

class Budget(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    category = db.Column(db.String(100))

    limit_amount = db.Column(db.Float)