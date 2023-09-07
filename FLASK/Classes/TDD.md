We will create the API from scratch with step-by-step instructions and explanations.

**Step 1: Setup**

Let's start by setting up the project structure and installing the required packages:

```bash
mkdir todo_api
cd todo_api
```

Create a virtual environment and activate it:

```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

Install Flask and pytest:

```bash
pip install Flask pytest
```

**Step 2: Create the Flask App**

Create a file named `app.py` for your Flask application:

```python
from flask import Flask, request, jsonify

app = Flask(__name__)

# Initialize an empty list to store tasks
tasks = []

@app.route('/tasks', methods=['GET'])
def get_tasks():
    """Get a list of tasks."""
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def create_task():
    """Create a new task."""
    data = request.get_json()
    if 'title' in data:
        task = {'title': data['title'], 'done': False}
        tasks.append(task)
        return jsonify(task), 201
    else:
        return jsonify({'error': 'Title is required'}), 400

if __name__ == '__main__':
    app.run(debug=True)
```

In this code, we have defined a Flask application with two routes:
- `/tasks` (GET): Returns a JSON list of tasks.
- `/tasks` (POST): Allows you to create a new task by sending a JSON payload with a "title" field.

**Step 3: Write the First Test**

Create a file named `test_app.py` for your tests. We'll start with a simple test for getting tasks:

```python
import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_empty_tasks(client):
    response = client.get('/tasks')
    assert response.status_code == 200
    assert response.json == []

def test_create_task(client):
    response = client.post('/tasks', json={'title': 'Buy groceries'})
    assert response.status_code == 201
    assert response.json == {'title': 'Buy groceries', 'done': False}
```

Here, we use the `pytest` framework to write tests. The first test checks if the `/tasks` endpoint returns an empty list initially, and the second test checks if we can create a task.

**Step 4: Run the Tests**

Run the tests by executing:

```bash
pytest test_app.py
```

Both tests should fail at this point.

**Step 5: Implement the Functionality**

Now, let's implement the functionality in `app.py` to make the tests pass:

```python
# Add these import statements at the top of app.py
from flask import Flask, request, jsonify

app = Flask(__name__)

# Initialize an empty list to store tasks
tasks = []

@app.route('/tasks', methods=['GET'])
def get_tasks():
    """Get a list of tasks."""
    return jsonify(tasks)

@app.route('/tasks', methods=['POST'])
def create_task():
    """Create a new task."""
    data = request.get_json()
    if 'title' in data:
        task = {'title': data['title'], 'done': False}
        tasks.append(task)
        return jsonify(task), 201
    else:
        return jsonify({'error': 'Title is required'}), 400

if __name__ == '__main__':
    app.run(debug=True)
```

**Step 6: Run the Tests Again**

Now that we've implemented the functionality, run the tests again:

```bash
pytest test_app.py
```

Both tests should pass.

**Step 7: Additional Tests**

Let's add more tests for completing tasks and handling errors:

```python
# In test_app.py, add the following tests:

def test_create_task_missing_title(client):
    response = client.post('/tasks', json={})
    assert response.status_code == 400
    assert response.json == {'error': 'Title is required'}

def test_create_task_and_complete_it(client):
    response = client.post('/tasks', json={'title': 'Finish homework'})
    assert response.status_code == 201
    assert response.json == {'title': 'Finish homework', 'done': False}

    response = client.put('/tasks/0', json={'done': True})
    assert response.status_code == 200
    assert response.json == {'title': 'Finish homework', 'done': True}

def test_create_task_and_get_task_by_id(client):
    response = client.post('/tasks', json={'title': 'Read a book'})
    assert response.status_code == 201
    assert response.json == {'title': 'Read a book', 'done': False}

    response = client.get('/tasks/0')
    assert response.status_code == 200
    assert response.json == {'title': 'Read a book', 'done': False}
```

**Step 8: Implement Additional Functionality**

Now, implement the additional functionality in `app.py`:

```python
# Add these routes to app.py

@app.route('/tasks/<int:task_id>', methods=['GET', 'PUT'])
def get_or_update_task(task_id):
    """Get or update a task by ID."""
    if task_id < 0 or task_id >= len(tasks):
        return jsonify({'error': 'Task not found'}), 404

    if request.method == 'GET':
        return jsonify(tasks[task_id])
    elif request.method == 'PUT':
        data = request.get_json()
        if 'done' in data:
            tasks[task_id]['done'] = data['done']
            return jsonify(tasks[task_id])
        else:
            return jsonify({'error': 'Done field is required'}), 400

if __name__ == '__main__':
    app.run(debug=True)
```

**Step 9: Run the Tests Again**

Run the tests once more:

```bash
pytest test_app.py
```

All tests should pass.

Congratulations! You've successfully implemented a simple To-Do list API using Flask and Test-Driven Development (TDD). 