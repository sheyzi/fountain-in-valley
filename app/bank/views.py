from flask import Blueprint, render_template, request, url_for, redirect, flash
from flask_login import current_user
from app import db
from app.models import User
from flask_login import login_required

from app.email import send_email

bank = Blueprint('bank', __name__)

@bank.route('/dashboard/')
@login_required
def dashboard():
    if not current_user.pin:
        return redirect(url_for('bank.create_pin'))
    return render_template('bank/dashboard.html')

@bank.route('/transfer/fountain/', methods=['GET', 'POST'])
def transfer_fountain():
    if not current_user.pin:
        return redirect(url_for('bank.create_pin'))

    if request.method == 'POST':
        acNo = request.form['account_number']
        amt = request.form['amount']
        pin = request.form['pin']

        if current_user.account_balance < float(amt):
            flash("Insufficient Balance", 'error')

        elif current_user.pin != pin:
            flash("Invalid Pin", 'error')

        elif not User.query.filter_by(account_number=acNo).first():
            flash("Incorrect account number", 'error')

        elif acNo == current_user.account_number:
            flash("You can't send money to yourself from your account... That's dumb as fuck!", 'error')

        else:
            targer_user = User.query.filter_by(account_number = acNo).first()
            targer_user.account_balance += float(amt)
            current_user -= float(amt)

            """
            TODO:
                1. Update transaction history for both users
                2. Send each users debit and credit alert respectively
                3. Save all changes to database
            """

    return render_template('bank/transfer_fountain.html')

@bank.route('/create-pin/', methods=['GET', 'POST'])
def create_pin():
    if current_user.pin:
        flash("Account has a pin already", 'info')
        return redirect(url_for('bank.dashboard'))
    if request.method == "POST":
        pin = request.form['pin']
        confirm_pin = request.form['confirm_pin']

        if len(pin) != 4:
            flash("Pin must be 4 characters", "error")
        elif pin != confirm_pin:
            flash("The pin must match", "error")
        else:
            current_user.pin = pin
            db.session.commit()
            flash("Pin created successfully", 'success')
            return redirect(url_for('bank.dashboard'))
    return render_template('bank/create_pin.html')