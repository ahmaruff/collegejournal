from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired
from ..models import Journal
from flask_pagedown.fields import PageDownField

class AddNewJournal(FlaskForm):
    title = StringField('Journal Title', validators=[DataRequired()])
    course_list = SelectField('Course', choices=[])
    body = PageDownField('Journal Body', validators=[DataRequired()])
    submit = SubmitField('Add new journal')

class EditJournal(FlaskForm):
    title = StringField('Journal Title', validators=[DataRequired()])
    course_list = SelectField('Course', choices=[])
    body = PageDownField('Journal Body', validators=[DataRequired()])
    submit = SubmitField('Edit journal')