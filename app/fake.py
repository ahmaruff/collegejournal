"""
Fake - Generate fake account & journal (for development purpose)

Function:
    users       : generate fake user account
    journals    : generate fake journal content

"""

from random import randint
from sqlalchemy.exc import IntegrityError
from faker import Faker
from app import db
from .models import Student, Journal, Course

def users(count=100):
    fake = Faker()
    i = 0
    while i < count:
        s = Student(email=fake.email(),
                    username=fake.user_name(),
                    password='password',
                    fullname=fake.name(),
                    confirmed=True
                    )
        db.session.add(s)
        try:
            db.session.commit()
            i+=1
        except IntegrityError:
            db.session.rollback()
def journals(count=100):
    fake=Faker()
    user_count = Student.query.count()
    for i in range(count):
        s = Student.query.offset(randint(0, user_count -1)).first()
        j = Journal(journal_title=fake.job(),
                    journal=fake.text(),
                    student=s,
                    course=Course.query.first())

        db.session.add(j)
    db.session.commit()