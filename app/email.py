from flask_mail import Message
from app import mail, config
from flask import render_template

def send_mail(to, subjects, template, **kwargs):
    msg = Message(subject='[CollegeJournal] '+subjects,
                    recipients=[to] )
    msg.body = render_template(template + '.txt', **kwargs)
    #msg.html = render_template(template + '.html', **kwargs)

    mail.send(msg)