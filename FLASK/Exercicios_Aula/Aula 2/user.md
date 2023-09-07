
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
