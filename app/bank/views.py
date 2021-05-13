from flask import Blueprint, render_template, request, url_for, redirect, flash
from flask_login import login_required

bank = Blueprint('bank', __name__)

@bank.route('/dashboard/')
@login_required
def dashboard():
    return render_template('bank/dashboard.html')