from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import Optional
from ..models import Student

class EditProfileForm(FlaskForm):
    fullname = StringField('Full Name', validators=[Optional()])
    department = StringField('Department/Major', validators=[Optional()])
    faculty = StringField('Faculty', validators=[Optional()])
    university = StringField('University', validators=[Optional()])
    about_me = TextAreaField('Bio', validators=[Optional()], default='Sedang Belajar')
    submit = SubmitField('Edit Profile')