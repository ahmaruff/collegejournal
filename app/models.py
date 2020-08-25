from app import db
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import login_manager
from  markdown import markdown
import bleach
from flask import current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


class Student(db.Model, UserMixin):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64), unique=True, index=True)
    username = db.Column(db.String(64), unique=True, index=True)
    fullname = db.Column(db.String(64), index=True)
    department = db.Column(db.String(64), nullable=True) #prodi
    faculty = db.Column(db.String(64), nullable=True)
    university = db.Column(db.String(64), nullable=True)
    about_me = db.Column(db.Text, nullable=True)
    courses = db.relationship('Course', secondary='journals')
    
    #confirmation token
    confirmed = db.Column(db.Boolean, default=False)

    def generate_confirmation_token(self, expiration=3600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'confirm' : self.id}).decode("utf-8")
    
    def confirm(self, token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            data = s.loads(token.encode("utf-8"))
        except:
            return False
        if data.get('confirm') != self.id:
            return False
        self.confirmed = True
        db.session.add(self)
        return True



    #pasword
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


    #reset password
    def generate_reset_password_token(self, expiration=600):
        s = Serializer(current_app.config['SECRET_KEY'], expiration)
        return s.dumps({'reset_password' : self.id}).decode("utf-8")
    
    @staticmethod
    def verify_reset_password_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            id = s.loads(token.encode("utf-8"))['reset_password']
        except:
            return False
        return Student.query.get(id)
        
    
    def __repr__(self):
        return '<Student %r>' % self.username

class Course(db.Model):
    __tablename__ = 'courses'
    id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(64),unique=True, index=True)
    semester = db.Column(db.Integer, index=True)

    students = db.relationship('Student', secondary='journals')

    def __repr__(self):
        return '<course %r>' % self.course_name


# many-to-many relationship + add journal column
class Journal(db.Model):
    __tablename__ = 'journals'
    id = db.Column(db.Integer, primary_key=True)

    # Foreign key to Student & Course table
    student_id = db.Column(db.Integer, db.ForeignKey('students.id'))
    course_id = db.Column(db.Integer, db.ForeignKey('courses.id'))
    
    # define relationship to table Student & Course table
    student = db.relationship('Student', backref=db.backref('journals', cascade='all, delete-orphan'))
    course = db.relationship('Course', backref=db.backref('journals', cascade='all, delete-orphan'))

    # Journal Column
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    journal_title = db.Column(db.String(64), index=True)
    journal = db.Column(db.Text) #kolom text deskripsi jurnal

    journal_html = db.Column(db.Text) # kolom cache markdown

    @staticmethod
    def on_changed_journal(target, value, oldvalue, initiator):
        allowed_tags = ['a', 'abbr', 'acronym', 'b', 'blockquote', 'code',
                        'em', 'i', 'li', 'ol', 'pre', 'strong', 'ul', 'h1',
                        'h2', 'h3', 'p',]
        target.journal_html = bleach.linkify(bleach.clean(\
            markdown(value, output_format='html'),
            tags=allowed_tags, strip=True))
    
    def __repr__(self):
        return '<journal %r>' % self.journal_title

db.event.listen(Journal.journal, 'set', Journal.on_changed_journal) #markdown cop

#user loader for authentication
@login_manager.user_loader
def load_user(user_id):
    return Student.query.get(int(user_id))