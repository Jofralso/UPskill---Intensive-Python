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