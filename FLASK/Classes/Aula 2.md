## Hour 9-12: Database Integration

### **Working with SQLite and SQLAlchemy**

- Flask supports multiple databases, but we'll start with SQLite, a simple database.
- To use SQLite, we'll integrate Flask with SQLAlchemy, an ORM (Object-Relational Mapping) library.

### **Creating Models and Database Tables**

- Models define the structure of our database tables.
- SQLAlchemy helps us create and interact with these tables.
- Let's create a simple User model:

```python
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
```

- Use `db.create_all()` to create database tables based on your models.

### **CRUD Operations with Databases**

- CRUD stands for Create, Read, Update, and Delete, which are fundamental database operations.
- Use SQLAlchemy queries to interact with the database.

```python
# Create a new user
new_user = User(username='john_doe', email='john@example.com')
db.session.add(new_user)
db.session.commit()

# Read from the database
user = User.query.filter_by(username='john_doe').first()

# Update data
user.email = 'new_email@example.com'
db.session.commit()

# Delete a user
db.session.delete(user)
db.session.commit()
```

### **Resources:**

- [SQLAlchemy documentation](https://docs.sqlalchemy.org/en/20/)
- [Flask-SQLAlchemy documentation](https://flask-sqlalchemy.palletsprojects.com/)

## Hour 13-16: User Authentication

### **User Registration and Login**

- Implementing user registration and login is essential for web applications.
- We'll use Flask-Login and Flask-Bcrypt for this purpose.

### **Password Hashing and Security**

- Storing plaintext passwords is a security risk.
- Flask-Bcrypt helps securely hash and verify passwords.

```python
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

# To hash a password before storing it
hashed_password = bcrypt.generate_password_hash('user_password').decode('utf-8')

# To check a password against the stored hash
if bcrypt.check_password_hash(user.password_hash, 'user_input_password'):
    # Passwords match
```

### **User Sessions**

- User sessions are essential for tracking user authentication across requests.
- Flask-Login provides session management.

```python
from flask_login import LoginManager, UserMixin, login_user, current_user, login_required, logout_user

login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Create a User model that extends UserMixin
class User(UserMixin, db.Model):
    # ...

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Logging in a user
user = User.query.get(1)
login_user(user)

# Checking if a user is logged in
if current_user.is_authenticated:
    # User is logged in

# Logging out a user
logout_user()
```

### **Resources:**

- [Flask-Login documentation](https://flask-login.palletsprojects.com/)
- [Flask-Bcrypt documentation](https://flask-bcrypt.readthedocs.io/)

---
