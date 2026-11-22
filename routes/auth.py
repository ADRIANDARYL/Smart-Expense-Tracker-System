from flask import Blueprint, render_template, redirect, url_for, flash
from forms import RegisterForm, LoginForm
from models import User
from extensions import db
from flask_login import login_user, logout_user
import bcrypt

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['GET', 'POST'])
def register():

    form = RegisterForm()
    
    if form.validate_on_submit():

        existing_email = User.query.filter_by(
            email=form.email.data
        ).first()

        existing_phone = User.query.filter_by(
            phone=form.phone.data
        ).first()

        if existing_email:
            flash('Email already exists')
            return redirect(url_for('auth.register'))
        
        if existing_phone:
            flash('Phone number already exists')
            return redirect(url_for('auth.register'))
        
        hashed_password = bcrypt.hashpw(
            form.password.data.encode('utf-8'), 
            bcrypt.gensalt()
        )

        new_user = User(
            username=form.username.data,
            email=form.email.data,
            phone=form.phone.data,
            password_hash=hashed_password.decode('utf-8')
        )

        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful.')

        return redirect(url_for('auth.login'))
    
    return render_template('register.html', form=form)


@auth.route('/login', methods=['GET', 'POST'])
def login():

    form = LoginForm()

    if form.validate_on_submit():

        user = User.query.filter_by(
            email=form.email.data
        ).first()

        if user and bcrypt.checkpw(
            form.password.data.encode('utf-8'), 
            user.password_hash.encode('utf-8')
        ):

            login_user(user)
            
            return redirect(url_for('dashboard.home'))
        
        flash('Invalid email or password.')

    return render_template('login.html', form=form)


@auth.route('/logout')
def logout():

    logout_user()

    return redirect(url_for('auth.login'))