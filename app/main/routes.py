import os
import secrets
from flask import render_template, request, url_for, flash, redirect
import app
from ..forms import BlogForm, RegistrationForm, LoginForm, UpdateAccountForm
from app import db
from app.main import main
from app.models import User, Blog
from flask_login import current_user, login_required, login_user, logout_user

blog = [
    {
        'author': 'Test User',
        'title': 'Test blog',
        'body': 'Test Tester Testing',
        'date_posted': 'May 6, 2020'
    },
    {
        'author': 'John User',
        'title': 'Johns blog',
        'body': 'John Tester Testing',
        'date_posted': 'May 2, 2020'
    }
]


@login_required
@main.route("/")
def index():
    blog = Blog.query.all()
    return render_template('index.html', blog=blog)


@main.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Account successfully created for {form.username.data}', 'success')
        return redirect(url_for('main.login'))
    return render_template('register.html', title='Register', form=form)


@main.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.index'))  # prevents the user from double logging in
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash(f'Not successful', 'danger')
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
    return redirect(url_for('main.logout'))


@main.route('/blog/new', methods=['GET', 'POST'])
def new_blog():
    form = BlogForm()
    if form.validate_on_submit():
        blog = Blog(title=form.title.data, body=form.body.data)
        db.session.add(blog)
        db.session.commit()
        flash('Your blog has been posted successfully!', 'success')
        return redirect(url_for('main.index'))
    return render_template('blog.html', title='New blog', form=form)


@main.route("/profile", methods=['GET', 'POST'])
@login_required
def profile():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.add(blog)
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('main.profile'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    return render_template('user.html', title='Profile', form=form)
