from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FloatField,  SubmitField
from wtforms.validators import DataRequired, Email, Length

class RegisterForm(FlaskForm):
    
    username = StringField('Username', validators=[DataRequired()])

    email = StringField('Email', validators=[
        DataRequired(), 
        Email()
    ])

    phone = StringField('Phone', validators=[DataRequired()])

    password = PasswordField('Password', validators=[
        DataRequired(), 
        Length(min=6)
    ])

    submit = SubmitField('Register')


class LoginForm(FlaskForm):

    email = StringField('Email', validators=[
        DataRequired(),
        Email()
    ])

    password = PasswordField('Password', validators=[
        DataRequired()
    ])

    submit = SubmitField('Login')


class ExpenseForm(FlaskForm):
    
    category = StringField('Category', validators=[DataRequired()])

    amount = FloatField('Amount', validators=[DataRequired()])

    description = StringField('Description')

    payment_method = StringField('Payment Method')

    submit = SubmitField('Add Expense')

    