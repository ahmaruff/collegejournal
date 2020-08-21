from flask import render_template, redirect, url_for, request, abort
from flask_login import login_required, current_user
from ..models import Journal, Student, Course
from .forms import AddNewJournal, EditJournal
from app import db
from datetime import datetime
from . import journal

@journal.route('/')
@login_required
def index():
    page = request.args.get('page', 1, type=int)
    pagination = Journal.query.filter_by(student_id=current_user.id)\
        .order_by(Journal.timestamp.desc()).paginate(page, per_page=5, error_out=False)  # per_page=current_app.config['FLASKY_POSTS_PER_PAGE']
    journals = pagination.items
    # journals = Journal.query.order_by(Journal.timestamp).all()
    return render_template('journal/index.html', pagination=pagination, journals=journals)

@journal.route('/<int:id>')
def journal_id(id):
    journal = Journal.query.get_or_404(id)
    md_text = journal.journal
    return render_template('journal/journal-item.html', journal=journal, md_text=md_text)


@journal.route('/add', methods=['GET','POST'])
@login_required
def add():
    form = AddNewJournal()
    form.course_list.choices = [(course.id, course.course_name) for course in Course.query.order_by(Course.semester).all()]

    if form.validate_on_submit():
        journal = Journal(journal_title=form.title.data,
                            journal=form.body.data,
                            course= Course.query.filter_by(id=form.course_list.data).first(),
                            student=current_user._get_current_object()
                            )
        db.session.add(journal)
        db.session.commit()
        return redirect(url_for('note.index'))
    return render_template('journal/add.html', form=form)

@journal.route('/edit/<int:id>', methods=['GET','POST'])
@login_required
def edit(id):
    journal = Journal.query.get_or_404(id)
    if current_user != journal.student:
        abort(403)
    form = EditJournal()
    form.course_list.choices = [(course.id, course.course_name) for course in Course.query.order_by(Course.semester).all()]
    
    if form.validate_on_submit():
        journal.journal_title=form.title.data
        journal.course = Course.query.filter_by(id=form.course_list.data).first()
        journal.journal = form.body.data
        db.session.add(journal)
        db.session.commit()
        return redirect(url_for('note.journal_id', id=journal.id))
    form.title.data = journal.journal_title
    form.course_list.data = journal.course
    form.body.data = journal.journal
    
    return render_template('journal/edit_journal.html', form=form, journal=journal)


@journal.route('remove/<int:id>', methods=['GET','POST'])
@login_required
def remove(id):
    journal = Journal.query.get_or_404(id)
    if current_user != journal.student:
        abort(403)
    db.session.delete(journal)
    db.session.commit()
    return redirect(url_for('journal.index'))