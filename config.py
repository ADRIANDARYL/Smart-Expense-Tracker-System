import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:

    SECRET_KEY = 'x7#Kp9@Lm2!Qa8$Uv5#SmartExpense2026'

    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(
        BASE_DIR,
        'expense_tracker.db'
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False