'''
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/v1/hello', methods=['GET'])
def get_hello():
    return jsonify(message='Hello, World!')

if __name__ == '__main__':
    app.run(debug=True)

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
    
    '''
    
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