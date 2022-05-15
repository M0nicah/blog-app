import os
import secrets
from flask import render_template, request, url_for, flash, redirect
from PIL import Image
import app
from ..forms import PitchForm, RegistrationForm, LoginForm, UpdateAccountForm
from app import db
from app.main import main
from app.models import User, Pitch
from flask_login import current_user, login_required, login_user, logout_user

pitch = [
    {
        'author': 'Test User',
        'title': 'Test Pitch',
        'body': 'Test Tester Testing',
        'date_posted': 'May 6, 2020'
    },
    {
        'author': 'John User',
        'title': 'Johns Pitch',
        'body': 'John Tester Testing',
        'date_posted': 'May 2, 2020'
    }
]


@login_required
@main.route("/")
def index():
    pitch = Pitch.query.all()
    return render_template('index.html', pitch=pitch)


@main.route("/signup", methods=['GET', 'POST'])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Account successfully created for {form.username.data}', 'success')
        return redirect(url_for('main.login'))
    return render_template('signup.html', title='Register', form=form)


@main.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))  # prevents the user from double logging in
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash(f'Not successfull', 'danger')
            return redirect(url_for('main.login'))
        login_user(user)
        flash(f'Login Successful', 'success')
        return redirect(url_for('main.index'))
    return render_template('login.html', title='Login', form=form)


@main.route('/logout')
def logout():
    '''
    Function that handles logout
    Returns:
        Log out user to login page
    '''
    logout_user()
    return redirect(url_for('main.login'))


@main.route('/pitch/new', methods=['GET', 'POST'])
def new_pitch():
    form = PitchForm()
    if form.validate_on_submit():
        pitch = Pitch(title=form.title.data, body=form.body.data)
        db.session.add(pitch)
        db.session.commit()
        flash('Your Pitch has been posted successfully!', 'success')
        return redirect(url_for('main.index'))
    return render_template('pitches.html', title='New Pitch', form=form)


@main.route("/profile", methods=['GET', 'POST'])
@login_required
def profile():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.add(pitch)
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('main.profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    return render_template('user.html', title='Profile', form=form)
