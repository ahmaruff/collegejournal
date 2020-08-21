from flask import render_template, redirect, url_for, flash
from . import course
from flask_login import login_required
from .forms import AddCourseForm
from ..models import Course
from app import db

# @course.route('/index')
# def index():
#     form = AddCourseForm()
#     courses = Course.query.all()
#     render_template('course/index.html', courses=courses, form=form)

@course.route('/index', methods=['GET','POST'])
@login_required
def index():
    form = AddCourseForm()
    if form.validate_on_submit():
        course = Course(course_name=form.course_name.data,
                        semester=form.semester.data)
        db.session.add(course)
        db.session.commit()
        flash('Course registered')
        return redirect(url_for('course.index'))
    courses = Course.query.order_by(Course.semester).all()
    return render_template('course/index.html', form=form, courses=courses)


@course.route('/remove/<id>', methods=['GET','POST'])
@login_required
def remove(id):
    course = Course.query.filter_by(id=int(id)).first()
    db.session.delete(course)
    db.session.commit()
    flash('Course has been removed')
    return redirect(url_for('course.index'))
