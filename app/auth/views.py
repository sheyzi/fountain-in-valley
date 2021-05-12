from flask import Blueprint, render_template, request, url_for, redirect,flash

auth = Blueprint('auth', __name__)

@auth.route('/login/', methods=['GET', 'POST'])
def login():
    return render_template('auth/login.html')

@auth.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == "POST":
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        middle_name = request.form['middle_name']
        flash(first_name, "success")
    return render_template('auth/register.html')