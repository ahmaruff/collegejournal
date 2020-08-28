from flask import render_template, redirect, url_for, flash
from . import main
from app import db
from flask_login import login_required, current_user
from app.models import Student, Journal
from .forms import EditProfileForm
from app import Markdown

@main.route('/')
@login_required
def index():
    latest_journal = Journal.query.filter_by(student_id=current_user.id).order_by(Journal.id.desc()).first()
    if latest_journal is None:
        md_text = 'random string and never showed up, btw'
    else:
        md_text = latest_journal.journal
    return render_template('main/index.html', latest_journal=latest_journal, md_text=md_text)


@main.route('/about')
def about():
    return render_template('main/about.html')

@main.route('/profile/<username>')
def profile(username):
    student = Student.query.filter_by(username=username).first_or_404()
    return render_template('main/profile.html', student=student)

@main.route('/edit-profile', methods=['GET','POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.fullname = form.fullname.data
        current_user.department = form.department.data
        current_user.faculty = form.faculty.data
        current_user.university = form.university.data
        current_user.about_me = form.about_me.data
        db.session.add(current_user._get_current_object())
        db.session.commit()
        flash('Your profile has been updated.', 'success')
        return redirect(url_for('main.profile', username=current_user.username))
    form.fullname.data = current_user.fullname
    form.department.data = current_user.department
    form.faculty.data = current_user.faculty
    form.university.data = current_user.university
    form.about_me.data = current_user.about_me
    return render_template('main/edit_profile.html', form=form)

@main.route('/markdown-guide')
def md():
    return render_template('main/markdown_guide.html')