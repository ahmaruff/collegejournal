from flask_mail import Message
from app import mail, config
from flask import render_template, current_app

from threading import Thread


def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


def send_mail(to, subjects, template, **kwargs):
    msg = Message(subject='[CollegeJournal] '+subjects,
                    recipients=[to] )
    msg.body = render_template(template + '.txt', **kwargs)
    #msg.html = render_template(template + '.html', **kwargs)

    Thread(target=send_async_email,
           args=(current_app._get_current_object(), msg)).start()

def send_resetpassword_req(to, **kwargs):
    msg = Message(subject='[College Journal] - Reset your password',
                            recipients=[to])
    msg.body = render_template('auth/email/resetpassword_req.txt', **kwargs)

    Thread(target=send_async_email,
           args=(current_app._get_current_object(), msg)).start()