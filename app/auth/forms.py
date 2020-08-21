from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, ValidationError
from wtforms.validators import DataRequired, Length, Email, EqualTo, Regexp
from ..models import Student

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1,64), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me Logged In')
    submit = SubmitField('Log In')

class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(1,64), Email()])
    username = StringField('Username', validators=[DataRequired(), Length(1,64),
                                                    Regexp('^[a-z][a-z0-9_.]*$', 0,
                                                    'Usernames must have only lowercase letters, numbers, dots or underscores')])
    fullname = StringField('Full Name', validators=[DataRequired(), Length(1,64)])
    
    password = PasswordField('Password',validators=[DataRequired(), EqualTo('password2', message='Password must match')])
    password2 = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Register')

    def validate_email(self, field):
        if Student.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered')
        
    def validate_username(self, field):
        if Student.query.filter_by(username=field.data).first():
            raise ValidationError('Username already registered')

    def validate_fullname(self, field):
        valid_name = field.data.title()
        if valid_name != field.data:
            raise ValidationError('Name  should be capitalize in each word (example : Valid Full Name)')



