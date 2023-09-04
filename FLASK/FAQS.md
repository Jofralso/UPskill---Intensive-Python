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

## Hour 9-12: Database Integration

### **Exercise 5: Building a To-Do List**

**Solution:**

```python
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite