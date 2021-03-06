import os
import secrets
from flask import render_template, request, url_for, flash, redirect
import app
from app.requests import process_quote
from ..forms import BlogForm, RegistrationForm, LoginForm, UpdateAccountForm
from app import db
from app.main import main
from app.models import User, Blog
from flask_login import UserMixin, current_user, login_required, login_user, logout_user

@login_required
@main.route("/")
def index():
    blog = Blog.query.all()
    quote = process_quote()
    return render_template('index.html', blog=blog, quote=quote)


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


@main.route('/posts/edit/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_post(id):
	blog_to_edit = Blog.query.get(id)
	form = BlogForm()
	if form.validate_on_submit():
		blog.title = form.title.data
		blog.body = form.body.data
		# Update Database
		db.session.add(blog_to_edit)
		db.session.commit()
		flash("Blog Has Been Updated!", 'info')
		return redirect(url_for('main.index'))
	
	if current_user.email == UserMixin.email or current_user.id == 14:
		form.title.data = blog.title
		form.body.data = blog.body
		return render_template('blog.html', form=form)
	else:
		flash("You Aren't Authorized To Edit This Post...")
		blog = Blog.query.order_by(blog.date_posted)
		return render_template("index.html", blog=blog)


@main.route('/blog/delete/<int:id>')
@login_required
def delete(id):
    blog_to_delete =  Blog.query.get(id)
    try: 
        db.session.delete(blog_to_delete)
        db.session.commit()
        flash('The blog post has been deleted.', 'info')
        return redirect(url_for('main.index'))
    except:
        flash('Whoops! An error occured. Cannot delete blog', 'danger')
    return render_template('index.html', title='New blog')


# @main.route("/profile", methods=['GET', 'POST'])
# @login_required
# def profile():
#     form = UpdateAccountForm()
#     if form.validate_on_submit():
#         current_user.username = form.username.data
#         current_user.email = form.email.data
#         db.session.add(User)
#         db.session.commit()
#         flash('Your account has been updated!', 'success')
#         return redirect(url_for('main.index'))
#     elif request.method == 'GET':
#         form.username.data = current_user.username
#         form.email.data = current_user.email
#     return render_template('user.html', title='Profile', form=form)
