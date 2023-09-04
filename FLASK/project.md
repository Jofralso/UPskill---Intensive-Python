

## Complex Flask Project: Task Management System

### Section 1: Introduction and Setup

**Tasks:**
- Set up a virtual environment and install Flask.
- Create a basic Flask application structure.

### Section 2: User Authentication and Authorization

**Tasks:**
- Implement user registration and login functionality.
- Use Flask-Login for managing user sessions.
- Create a user model using SQLAlchemy.

### Section 3: Templates and Frontend

**Tasks:**
- Design a user-friendly frontend using HTML and CSS.
- Use Jinja2 templates for dynamic rendering of user-specific data.

### Section 4: Task Creation and Display

**Tasks:**
- Allow users to create tasks with due dates and descriptions.
- Display a list of tasks for each user.

### Section 5: Database Integration

**Tasks:**
- Use SQLAlchemy to create models for tasks.
- Establish relationships between users and tasks.

### Section 6: RESTful APIs

**Tasks:**
- Create API routes for retrieving and updating tasks.
- Use Flask-RESTful to implement API resources.

### Section 7: Task Status and Progress

**Tasks:**
- Implement task status (e.g., "To Do," "In Progress," "Completed").
- Allow users to update the status of their tasks.

### Section 8: Deployment

**Tasks:**
- Deploy the application on a cloud platform like Heroku or AWS.
- Set up a production-ready database (e.g., PostgreSQL).

# Solution:

### Section 1: Introduction and Setup

1. **Set Up Virtual Environment and Install Flask:**
   - Create a new directory for your project.
   - Create and activate a virtual environment.
   - Install Flask using `pip install Flask`.

2. **Basic Flask Application Structure:**
   - Create a new file named `app.py` in your project directory.
   - Import Flask and create a basic Flask application:

```python
from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run()
```

### Section 2: User Authentication and Authorization

1. **User Model and Database Setup:**
   - Install necessary packages: `pip install Flask-Login Flask-SQLAlchemy`.
   - Set up the database:

```python
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task_management.db'
db = SQLAlchemy(app)
```

   - Create the User model:

```python
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    # Add more fields as needed
```

2. **User Registration and Login:**
   - Install `bcrypt` package: `pip install bcrypt`.
   - Implement user registration and login using Flask forms.

```python
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        hashed_password = bcrypt.generate_password_hash(request.form.get('password')).decode('utf-8')
        new_user = User(username=request.form.get('username'), password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html')

# Implement login route and functionality similarly
```

3. **User Sessions and Logout:**
   - Use Flask-Login to manage user sessions.
   - Implement a logout route:

```python
from flask_login import LoginManager, login_user, logout_user, login_required, current_user

login_manager = LoginManager(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))
```

### Section 3: Templates and Frontend
---
1. **Design Frontend:**
   - Create a directory named `templates` in your project directory.
   - Design HTML templates using Jinja2 templating for different pages (e.g., login, registration, dashboard).

---

### Section 4: Task Creation and Display

1. **Task Model and Relationships:**
   - Create a Task model with relationships to the User model:

```python
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200))
    due_date = db.Column(db.Date)
    status = db.Column(db.String(20), default='To Do')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
```

2. **Create and Display Tasks:**
   - Implement routes for creating tasks and displaying them for each user:

```python
@app.route('/tasks', methods=['GET', 'POST'])
@login_required
def tasks():
    if request.method == 'POST':
        new_task = Task(title=request.form.get('title'), description=request.form.get('description'), due_date=request.form.get('due_date'), user_id=current_user.id)
        db.session.add(new_task)
        db.session.commit()
    user_tasks = Task.query.filter_by(user_id=current_user.id).all()
    return render_template('tasks.html', tasks=user_tasks)
```
---

### Section 5: Database Integration

1. **Database Migration:**
   - Install Flask-Migrate: `pip install Flask-Migrate`.
   - Create and apply database migrations:

```python
from flask_migrate import Migrate

migrate = Migrate(app, db)
```

   - Run migrations: `flask db init`, `flask db migrate`, `flask db upgrade`.

### Section 6: RESTful APIs

1. **API for Tasks:**
   - Install Flask-RESTful: `pip install Flask-RESTful`.
   - Implement a RESTful API for tasks:

```python
from flask_restful import Api, Resource

api = Api(app)

class TaskResource(Resource):
    def get(self, task_id):
        task = Task.query.get(task_id)
        if task:
            return {'title': task.title, 'description': task.description, 'due_date': task.due_date, 'status': task.status}
        return {'message': 'Task not found'}, 404

api.add_resource(TaskResource, '/api/task/<int:task_id>')
```

### Section 7: Task Status and Progress

1. **Update Task Status:**
   - Implement routes for updating task status:

```python
@app.route('/tasks/<int:task_id>/update_status/<string:new_status>', methods=['POST'])
@login_required
def update_status(task_id, new_status):
    task = Task.query.get(task_id)
    if task and task.user_id == current_user.id:
        task.status = new_status
        db.session.commit()
    return redirect(url_for('tasks'))
```

### Section 8: Deployment

1. **Deploy on Heroku:**
   - Install `gunicorn`: `pip install gunicorn`.
   - Create a `Procfile` in your project directory: `web: gunicorn app:app`.
   - Set up a Heroku app and deploy using Git.

