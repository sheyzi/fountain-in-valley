import random
from flask import Blueprint, render_template, request, url_for, redirect,flash
from app import email
from app.models import User
from app import bcrypt
from flask_login import login_user, logout_user, current_user
from app import db

from app.email import send_email

auth = Blueprint('auth', __name__)

@auth.route('/')
def home():
    return redirect(url_for('bank.dashboard'))

@auth.route('/login/', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash("You are already logged in", "info")
        return redirect(url_for("bank.dashboard"))

    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

        next_page = request.args.get('next')

        if User.query.filter_by(email=username).first() and bcrypt.check_password_hash(User.query.filter_by(email=username).first().password, password):
            flash("Login Succesful", "success")
            user = User.query.filter_by(email=username).first()
            login_user(user)
            return redirect(next_page) if next_page else redirect(url_for('bank.dashboard'))
        elif User.query.filter_by(phone_number=username).first() and bcrypt.check_password_hash(User.query.filter_by(phone_number=username).first().password, password):
            flash("Login Succesful", "success")
            user = User.query.filter_by(phone_number=username).first()
            login_user(user)
            return redirect(next_page) if next_page else redirect(url_for('bank.dashboard'))
        else:
            flash("Incorrect credentials", "error")

    return render_template('auth/login.html')

@auth.route('/register/', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        flash("You are already logged in", "info")
        return redirect(url_for("bank.dashboard"))
        
    if request.method == "POST":
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        middle_name = request.form['middle_name']
        email = request.form['email']
        phone_number = request.form['phone_number']
        password1 = request.form['password']
        password2 = request.form['confirm_password']
        account_number = random.randint(1111111111, 1999999999)

        if User.query.filter_by(email=email).first():
            flash("Account with this email already exists", "error")

        elif User.query.filter_by(phone_number=phone_number).first():
            flash("Account with this phone number already exists", "error")

        elif len(first_name) < 3:
            flash("First name cannot be less than 3 characters", "error")

        elif len(last_name) < 3:
            flash("Last name cannot be less than 3 characters", "error")

        elif password1 != password2:
            flash("Passwords must be equal", "error")

        else:
            new_user = User()
            new_user.first_name = first_name
            new_user.last_name = last_name
            if len(middle_name) > 0:
                new_user.middle_name = middle_name
            new_user.email = email
            new_user.phone_number = phone_number
            new_user.account_number = account_number
            new_user.password = bcrypt.generate_password_hash(password1).decode('utf-8')

            db.session.add(new_user)
            db.session.commit()

            send_email(new_user.email, "Fountain in valley - Account Login Details", 'open_account.html', user=new_user, login_html=f"{request.host}/login")
            send_email(new_user.email, "Fountain in valley - Account Number", 'account_number.html', user=new_user, login_link=f"{request.host}/login")

            flash("Account created succesfully!! Login to access your details!", "success")
            return redirect(url_for('auth.login'))

             
                
        
    return render_template('auth/register.html')

@auth.route('/logout/')
def logout():
    logout_user()
    flash("Logged out successfully!!", "success")
    return redirect(url_for('auth.login'))