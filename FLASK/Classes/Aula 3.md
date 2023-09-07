## Hour 17-20: RESTful APIs with Flask

### **Introduction to REST Architecture**

- REST (Representational State Transfer) is an architectural style for designing networked applications.
- It emphasizes stateless communication between clients and servers.
- Resources are identified by URIs, and interactions are based on standard HTTP methods.

### **Building RESTful APIs with Flask**

**Example 1: Creating a Simple RESTful API**

**Solution:**

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/v1/hello', methods=['GET'])
def get_hello():
    return jsonify(message='Hello, World!')

if __name__ == '__main__':
    app.run(debug=True)
```

**Example 2: Handling GET Requests with Parameters**

**Solution:**

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

data = {'1': 'apple', '2': 'banana', '3': 'cherry'}

@app.route('/api/v1/fruits/<fruit_id>', methods=['GET'])
def get_fruit(fruit_id):
    if fruit_id in data:
        return jsonify(fruit=data[fruit_id])
    else:
        return jsonify(error='Fruit not found'), 404

if __name__ == '__main__':
    app.run(debug=True)
```

**Example 3: Handling POST Requests**

**Solution:**

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

data = {}

@app.route('/api/v1/fruits', methods=['POST'])
def add_fruit():
    if 'id' in request.json and 'name' in request.json:
        fruit_id = str(request.json['id'])
        fruit_name = request.json['name']
        data[fruit_id] = fruit_name
        return jsonify(message='Fruit added successfully'), 201
    else:
        return jsonify(error='Invalid data'), 400

if __name__ == '__main__':
    app.run(debug=True)
```

**Example 4: Handling PUT and DELETE Requests**

**Solution:**

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

data = {'1': 'apple', '2': 'banana', '3': 'cherry'}

@app.route('/api/v1/fruits/<fruit_id>', methods=['PUT'])
def update_fruit(fruit_id):
    if fruit_id in data and 'name' in request.json:
        data[fruit_id] = request.json['name']
        return jsonify(message='Fruit updated successfully')
    else:
        return jsonify(error='Invalid data or fruit not found'), 400

@app.route('/api/v1/fruits/<fruit_id>', methods=['DELETE'])
def delete_fruit(fruit_id):
    if fruit_id in data:
        del data[fruit_id]
        return jsonify(message='Fruit deleted successfully')
    else:
        return jsonify(error='Fruit not found'), 404

if __name__ == '__main__':
    app.run(debug=True)
```

### **JSON Responses**

- JSON (JavaScript Object Notation) is a lightweight data interchange format.
- Flask can easily handle JSON data for both incoming requests and outgoing responses.
- `jsonify` is used to create JSON responses.

Fully functioning example of a simple RESTful API for a "To-Do List" application using Flask. In this example, we'll create, read, update, and delete tasks.

Here's the code for the Flask application:

```python
from flask import Flask, jsonify, request

app = Flask(__name__)

# Initial data (in-memory database)
tasks = {
    1: {"task": "Buy groceries", "completed": False},
    2: {"task": "Finish homework", "completed": True},
    3: {"task": "Read a book", "completed": False},
}
next_task_id = 4

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify(tasks)

@app.route('/api/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = tasks.get(task_id)
    if task is None:
        return jsonify(error="Task not found"), 404
    return jsonify(task)

@app.route('/api/tasks', methods=['POST'])
def create_task():
    global next_task_id
    data = request.json
    task = {
        "task": data.get("task"),
        "completed": False,
    }
    tasks[next_task_id] = task
    next_task_id += 1
    return jsonify(message="Task created successfully"), 201

@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = tasks.get(task_id)
    if task is None:
        return jsonify(error="Task not found"), 404
    data = request.json
    task["task"] = data.get("task")
    task["completed"] = data.get("completed", False)
    return jsonify(message="Task updated successfully")

@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = tasks.get(task_id)
    if task is None:
        return jsonify(error="Task not found"), 404
    del tasks[task_id]
    return jsonify(message="Task deleted successfully")

if __name__ == '__main__':
    app.run(debug=True)
```

This Flask application provides the following API endpoints:

- `GET /api/tasks`: Retrieve all tasks.
- `GET /api/tasks/<task_id>`: Retrieve a specific task by ID.
- `POST /api/tasks`: Create a new task.
- `PUT /api/tasks/<task_id>`: Update an existing task.
- `DELETE /api/tasks/<task_id>`: Delete a task by ID.

To interact with this API, you can use tools like `curl`, Postman, or build a simple front-end application to perform CRUD operations on the to-do list.

For example, to create a new task using `curl`:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"task": "Walk the dog"}' http://localhost:5000/api/tasks
```

This example demonstrates the basics of building a RESTful API with Flask. You can expand upon this foundation to create more complex applications with additional features and data storage.

## Hour 21-24: Flask Extensions

### **Overview of Popular Flask Extensions**

- Flask has a rich ecosystem of extensions that add functionality to your applications.
- Extensions cover various areas, including authentication, email handling, file uploads, and more.
- These extensions simplify common tasks and enhance Flask's capabilities.

**Example 1: Sending Emails with Flask-Mail**

**Solution:**

```python
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'your_username'
app.config['MAIL_PASSWORD'] = 'your_password'

mail = Mail(app)

@app.route('/send_email', methods=['GET', 'POST'])
def send_email():
    if request.method == 'POST':
        recipient = request.form['recipient']
        subject = request.form['subject']
        message_body = request.form['message_body']
        msg = Message(subject=subject, recipients=[recipient])
        msg.body = message_body
        try:
            mail.send(msg)
            flash('Email sent successfully!', 'success')
        except Exception as e:
            flash(f'Email could not be sent: {str(e)}', 'danger')
    return render_template('email_form.html')

if __name__ == '__main__':
    app.run(debug=True)
```

**Example 2: Handling File Uploads with Flask-Uploads**

**Solution:**

```python
from flask import Flask, render_template, request, flash, redirect, url_for
from flask_uploads import UploadSet, configure_uploads, IMAGES

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['UPLOADS_DEFAULT_DEST'] = 'uploads'

images = UploadSet('images', IMAGES)
configure_uploads(app, images)

@app.route('/upload_image', methods=['GET', 'POST'])
def upload_image():
    if request.method == 'POST' and 'image' in request.files:
        image = request.files['image']
        if image:
            image_path = images.save(image)
            flash(f'Image saved as {image_path}', 'success')
        else:
            flash('No image selected', 'danger')
    return render_template('image_upload.html')

if __name__ == '__main__':
    app.run(debug=True)
```

### Simple Example: Real-Time Chat

In this basic example, we'll create a real-time chat application where users can join a chat room and exchange messages.

```python
from flask import Flask, render_template
from flask_socketio import SocketIO, join_room, leave_room, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('join')
def handle_join(data):
    room = data['room']
    join_room(room)
    emit('message', f'User {data["username"]} has joined the room.', room=room)

@socketio.on('leave')
def handle_leave(data):
    room = data['room']
    leave_room(room)
    emit('message', f'User {data["username"]} has left the room.', room=room)

@socketio.on('message')
def handle_message(data):
    room = data['room']
    message = data['message']
    emit('message', f'{data["username"]}: {message}', room=room)

if __name__ == '__main__':
    socketio.run(app, debug=True)
```

In this simple chat application:

- Users can join and leave chat rooms.
- Messages sent by users are broadcasted to others in the same room.

### Intermediate Example: Real-Time Notifications

In this intermediate example, we'll create a notification system that sends real-time updates to connected clients.

```python
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    emit('notification', 'A user has connected.')

@socketio.on('disconnect')
def handle_disconnect():
    emit('notification', 'A user has disconnected.')

if __name__ == '__main__':
    socketio.run(app, debug=True)
```

In this intermediate example:

- Clients receive notifications when users connect or disconnect.
- It demonstrates broadcasting messages to all connected clients.

### Complex Example: Real-Time Collaborative Drawing

In this complex example, we'll create a collaborative drawing application where multiple users can draw together on a shared canvas in real-time.

```python
from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('draw')
def handle_draw(data):
    emit('draw', data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, debug=True)
```

In this complex example:

- Users can draw on a shared canvas.
- The canvas updates in real-time for all connected users.
- It showcases the real-time synchronization of user actions.

---
I apologize for the oversight. Indeed, to complete these examples, you would need corresponding HTML templates and potentially JavaScript code for the frontend to interact with the Flask-SocketIO backend. Here are the basic HTML templates for each example:

### Simple Example: Real-Time Chat (index.html)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Real-Time Chat</title>
</head>
<body>
    <div id="chat">
        <ul id="messages"></ul>
        <input id="message_input" autocomplete="off" /><button onclick="sendMessage()">Send</button>
    </div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.0.1/socket.io.js"></script>
    <script>
        var socket = io.connect('http://' + document.domain + ':' + location.port);

        socket.on('message', function(msg) {
            var ul = document.getElementById('messages');
            var li = document.createElement('li');
            li.appendChild(document.createTextNode(msg));
            ul.appendChild(li);
        });

        function sendMessage() {
            var message = document.getElementById('message_input').value;
            socket.emit('message', { message: message });
            document.getElementById('message_input').value = '';
        }
    </script>
</body>
</html>
```

### Intermediate Example: Real-Time Notifications (index.html)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Real-Time Notifications</title>
</head>
<body>
    <div id="notifications"></div>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.0.1/socket.io.js"></script>
    <script>
        var socket = io.connect('http://' + document.domain + ':' + location.port);

        socket.on('notification', function(msg) {
            var div = document.getElementById('notifications');
            var p = document.createElement('p');
            p.appendChild(document.createTextNode(msg));
            div.appendChild(p);
        });
    </script>
</body>
</html>
```

### Complex Example: Real-Time Collaborative Drawing (index.html)

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Real-Time Drawing</title>
</head>
<body>
    <canvas id="canvas" width="800" height="400"></canvas>

    <script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.0.1/socket.io.js"></script>
    <script>
        var socket = io.connect('http://' + document.domain + ':' + location.port);
        var canvas = document.getElementById('canvas');
        var ctx = canvas.getContext('2d');

        var drawing = false;

        canvas.addEventListener('mousedown', startDrawing);
        canvas.addEventListener('mouseup', stopDrawing);
        canvas.addEventListener('mousemove', draw);

        socket.on('draw', function(data) {
            drawLine(data);
        });

        function startDrawing(e) {
            drawing = true;
            ctx.beginPath();
            ctx.moveTo(e.clientX - canvas.getBoundingClientRect().left, e.clientY - canvas.getBoundingClientRect().top);
        }

        function stopDrawing() {
            drawing = false;
            ctx.closePath();
        }

        function draw(e) {
            if (!drawing) return;
            ctx.lineTo(e.clientX - canvas.getBoundingClientRect().left, e.clientY - canvas.getBoundingClientRect().top);
            ctx.stroke();
            socket.emit('draw', { x: e.clientX - canvas.getBoundingClientRect().left, y: e.clientY - canvas.getBoundingClientRect().top });
        }

        function drawLine(data) {
            ctx.beginPath();
            ctx.moveTo(data.x, data.y);
            ctx.lineTo(data.x, data.y);
            ctx.stroke();
            ctx.closePath();
        }
    </script>
</body>
</html>
```

These HTML templates provide the frontend part of each example, allowing users to interact with the Flask-SocketIO backend. You can expand upon these templates to customize the look and feel of your real-time applications.