## Hour 1-4: Introduction to Flask

### **Exercise 1: Adding More Routes**

- Create a Flask application with routes for `/about`, `/contact`, and `/blog`.
- Each route should render a different HTML template with appropriate content.

### **Exercise 2: Dynamic Routing**

- Create a route that accepts a username as a parameter (e.g., `/profile/<username>`).
- Render a template that displays a personalized greeting using the provided username.

### **Example: Rendering Lists**

- Create a route that renders an HTML template to display a list of items (e.g., a list of books, movies, or products).
- Pass a list of items to the template and use Jinja2 to render them in an ordered or unordered list.

## Hour 5-8: Handling Forms and User Input

### **Exercise 3: Creating a Contact Form**

- Create a Flask application that includes a contact form.
- The form should have fields for name, email, and message.
- Implement form validation to ensure all fields are filled out before submission.
- Display a success message after successful form submission.

### **Exercise 4: User Registration Form**

- Create a Flask application with a user registration form.
- The form should include fields for username, email, password, and password confirmation.
- Implement form validation to check for a valid email format and matching passwords.
- After successful registration, store user data in a database or print it to the console.

### **Example: Uploading Files**

- Create a route that allows users to upload a file (e.g., an image or document).
- Handle file uploads using Flask's request object and store the uploaded file on the server.

## Hour 9-12: Database Integration

### **Exercise 5: Building a To-Do List**

- Create a Flask application for managing a to-do list.
- Use SQLAlchemy to define a "Task" model with fields like title, description, and completion status.
- Implement CRUD operations to create, read, update, and delete tasks.
- Display the list of tasks on the web page and provide options to add, edit, and delete tasks.

### **Exercise 6: Blogging Platform**

- Develop a simple blogging platform using Flask and SQLAlchemy.
- Create models for "User" and "Post" (with fields like title and content).
- Implement user registration and login functionality.
- Allow registered users to create, edit, and delete their blog posts.
- Display a list of blog posts on the homepage.

## Hour 13-16: User Authentication

### **Exercise 7: Password Reset**

- Implement a password reset feature for registered users.
- Allow users to request a password reset email with a unique token.
- When users click on the reset link in their email, they should be able to set a new password.

### **Exercise 8: User Profile**

- Create user profile pages that display user information and their authored blog posts.
- Ensure that only authenticated users can access their own profiles.
- Implement an "Edit Profile" feature for users to update their information.

### **Example: Role-Based Authentication**

- Extend your Flask application to include role-based authentication.
- Define roles (e.g., "User" and "Admin").
- Restrict certain routes and actions to specific roles (e.g., only admins can delete posts).

Certainly! Here are the exercises and examples with solutions for the Flask lesson:

## Hour 1-4: Introduction to Flask

### **Exercise 1: Adding More Routes**

**Solution:**

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the home page."

@app.route('/about')
def about():
    return "This is the About page."

@app.route('/contact')
def contact():
    return "Contact us at contact@example.com."

@app.route('/blog')
def blog():
    return "Check out our latest blog posts."

if __name__ == '__main__':
    app.run()
```

### **Exercise 2: Dynamic Routing**

**Solution:**

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the home page."

@app.route('/about')
def about():
    return "This is the About page."

@app.route('/contact')
def contact():
    return "Contact us at contact@example.com."

@app.route('/blog')
def blog():
    return "Check out our latest blog posts."

@app.route('/profile/<username>')
def profile(username):
    return render_template('profile.html', username=username)

if __name__ == '__main__':
    app.run()
```

### **Example: Rendering Lists**

**Solution:**

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    items = ['Item 1', 'Item 2', 'Item 3']
    return render_template('list.html', items=items)

if __name__ == '__main__':
    app.run()
```

## Hour 5-8: Handling Forms and User Input

### **Exercise 3: Creating a Contact Form**

**Solution:**

```python
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    message = StringField('Message', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        flash('Your message has been sent!', 'success')
        return redirect(url_for('contact'))
    return render_template('contact.html', form=form)

if __name__ == '__main__':
    app.run()
```

### **Exercise 4: User Registration Form**

**Solution:**

```python
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
bcrypt = Bcrypt(app)

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password

users = []

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        users.append(user)
        flash('Your account has been created! You can now log in.', 'success')
        return redirect(url_for('register'))
    return render_template('register.html', form=form)

if __name__ == '__main__':
    app.run()
```

### **Example: Uploading Files**

**Solution:**

```python
from flask import Flask, render_template, request, flash, redirect, url_for
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['UPLOAD_FOLDER'] = 'uploads'

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part', 'danger')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file', 'danger')
            return redirect(request.url)
        if file:
            filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filename)
            flash('File successfully uploaded', 'success')
            return redirect(request.url)
    return render_template('upload.html')

if __name__ == '__main__':
    app.run()
```

