from threading import Thread
from flask import current_app, render_template
from flask_mail import Message
from app import mail

def send_async_mail(app, msg):
    with app.app_context():
        print('======> Sending async mail')
        mail.send(msg)

def send_email(to, subject, template, **kwargs):
    app = current_app._get_current_object()
    msg = Message(subject, recipients=[to])
    msg.html = render_template('email/'+template, **kwargs)
    thr = Thread(target=send_async_mail, args=[app, msg])
    thr.start()
    return thr