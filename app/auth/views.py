from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from . import auth
from .forms import LoginForm, RegistrationForm, ResetPasswordRequest, ResetPasswordForm
from ..models import Student
from app import db
from ..email import send_mail, send_resetpassword_req

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Student.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            next = request.args.get('next')
            if next is None or not  next.startswith('/'):
                next = url_for('main.index')
            return redirect(next)
        flash('Invalid email or password', 'danger')
    return render_template('auth/login.html', form=form)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('you have been logged out', 'info')
    return redirect(url_for('main.index'))


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = Student(email=form.email.data,
                        username=form.username.data,
                        fullname=form.fullname.data,
                        password=form.password.data)
        db.session.add(user)
        db.session.commit()
        token = user.generate_confirmation_token()
        send_mail(user.email, 'Confirm your account', 
                    'auth/email/confirm', user=user, token=token)
        flash('You can now login', 'success')
        return redirect(url_for('auth.login'))
    return render_template('auth/register.html', form=form)


@auth.route('/confirm/<token>')
@login_required
def confirm(token):
    if current_user.confirmed:
        return redirect(url_for('main.index'))
    if current_user.confirm(token):
        db.session.commit()
        flash('You have confirmed your account. Thanks!', 'success')
    else:
        flash('The confirmation link is invalid or has expired.', 'warning')
    return redirect(url_for('main.index'))
    
@auth.route('/confirm')
@login_required
def resend_confirmation():
    token = current_user.generate_confirmation_token()
    send_mail(current_user.email, 'Confirm Your account',
                'auth/email/confirm', user=current_user, token=token)
    flash('A new confirmation email has been sent to you by email.', 'info')
    return redirect(url_for('main.index'))

@auth.before_app_request
def before_request():
    if current_user.is_authenticated \
        and not current_user.confirmed \
        and request.blueprint != 'auth' \
        and request.endpoint != 'static' :
        return redirect(url_for('auth.unconfirmed'))

@auth.route('/unconfirmed')
def unconfirmed():
    if current_user.is_anonymous or current_user.confirmed :
        return redirect(url_for('main.index'))
    return render_template('auth/unconfirmed.html')


@auth.route('/resetpassword_req', methods=['GET','POST'])
def resetpassword_req():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    form = ResetPasswordRequest()
    if form.validate_on_submit():
        user = Student.query.filter_by(email=form.email.data).first()
        if user:
            token = user.generate_reset_password_token()
            send_resetpassword_req(user.email, user=user, token=token)
        flash('Check your email for the instructions to reset your password')
        return redirect(url_for('auth.login'))
    return render_template('auth/resetpassword_req.html', form=form)


@auth.route('/reset_password/<token>', methods=['GET','POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))
    user = Student.verify_reset_password_token(token)
    if not user:
        return redirect(url_for('main.index'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.password = form.password.data
        db.session.add(user)
        db.session.commit()
        flash('Your password has been reset.')
        return redirect(url_for('auth.login'))
    return render_template('auth/resetpassword.html', form=form)


