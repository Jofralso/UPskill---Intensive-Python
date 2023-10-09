# -----------------------   Setup Flask application w/ SQLAlchemy and SQLite database    ------------------

from flask import Flask, render_template, request, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy

# for login 
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user, user_logged_in

# for forms and validation
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length
from werkzeug.security import generate_password_hash, check_password_hash

# for password policies
import re

from flask_limiter import Limiter

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///myblog_database.db"
app.config['SECRET_KEY'] = "your_secret_key"

# Secure your session cookies by setting them to be HttpOnly and Secure. This helps protect against session hijacking.
app.config['SESSION_COOKIE_HTTPONLY'] = True
app.config['SESSION_COOKIE_SECURE'] = True

# Implement rate limiting to prevent brute force attacks and IP whitelisting to restrict access to specific IPs if necessary.
'''limiter = Limiter(app, key_func=get_remote_address)'''



db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

'''
# Verify if password is valid
def is_valid_password(password):
    if not re.search("[a-z]", password):
        return False
    elif not re.search("[A-Z]", password):
        return False
    elif not re.search("[0-9]", password):
        return False
    elif not re.search("[_@$]" , password):
        return False
    else:
        return True
'''

############################             MODELS             ####################################
# -----------------------    User model  ----------------------------------------------------------------

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique = True, nullable = False)
    password = db.Column(db.String(60), nullable = False)
    posts = db.relationship('Post', backref='author', lazy=True)

    


# -----------------------    Post model ----------------------------------------------------------------

class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(80), nullable = False)
    content = db.Column(db.Text, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    # author = db.Column(db.String(80), nullable = False)

############################             FORMS             ####################################

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()]) # + , Email()
    message = TextAreaField('Message', validators=[DataRequired()])
    submit = SubmitField('Submit')


# -----------------------    Implement Form Validation (Flask - WTF)       ---------------------------------------------------------

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Create Post')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])


# Create the database
with app.app_context():
    db.create_all()

# Login Manager Configuration
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

############################             ROUTES             ####################################

@app.route('/')
def home():
    posts = Post.query.all()
    user_logged_in = session.get('user_logged_in', False)
    return render_template('home.html', posts = posts, user_logged_in = user_logged_in)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        flash('Your message has been successfully sent!', 'Sucess')
        return redirect(url_for('contact'))
    return render_template('contact.html', form= form)


@app.route('/about')
def about():
    return render_template('about.html')


# -----------------------    Individual Dashboard  ----------------------------------------------------------------

@app.route('/dashboard')
@login_required
def dashboard():
    user_logged_in = session.get('user_logged_in', False)
    user_posts = current_user.posts
    return render_template('dashboard.html', user_posts = user_posts, user_logged_in = user_logged_in)



@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))

    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        flash('Your account has been created! You can now log in.', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/edit_post/<int:post_id>', methods=['GET', 'POST'])
@login_required
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        return redirect(url_for('dashboard'))

    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.content = form.content.data
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('dashboard'))
    elif request.method == 'GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template('edit_post.html', form=form)



@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))

    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid username or password', 'danger')
    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


# -----------------------    Creating a new blog post. ----------------------------------------------------------------
@app.route('/create_post', methods = ['GET', 'POST']) #colocar os metodos GET porque vamos obter info e POST porque vamos inserir la info
@login_required
def create_post():
    # Form Validation Object
    form = PostForm()
    if form.validate_on_submit():
        title = form.title.data
        content = form.content.data
        author = current_user
        
        # save user data in database
        post = Post(title = title, content = content, author = author)
        db.session.add(post)
        db.session.commit()
        flash('Post Created!', 'success')
        return redirect(url_for('dashboard'))
    return render_template('create_post.html', form = form)



@app.route('/delete_post/<int:post_id>', methods=['GET', 'POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    if post.author != current_user:
        flash("You don't have permission to delete this post.", 'danger')
        return redirect(url_for('dashboard'))
    
    if request.method == 'POST':
        db.session.delete(post)
        db.session.commit()
        flash('Your post has been deleted!', 'success')
        return redirect(url_for('dashboard'))

    return render_template('delete_post.html', post=post)


'''
@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    db.session.pop('username', None)
    db.session.pop('password', None)
    return redirect(url_for('index'))

'''

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)