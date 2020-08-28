from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Regexp
from ..models import Course

class AddCourseForm(FlaskForm):
    course_name = StringField('Course Name', validators=[DataRequired()])
    semester = IntegerField('Semester', validators=[DataRequired()])
    submit = SubmitField('Add new course')

    def validate_course_name(self, field):
        if Course.query.filter_by(course_name=field.data).first():
            raise ValidationError('Course already registered')
        
        valid_name = field.data.title()
        if valid_name != field.data:
            raise ValidationError('Course name  should be capitalize in each word and does not contains special character (example : Valid Course Name)')
    