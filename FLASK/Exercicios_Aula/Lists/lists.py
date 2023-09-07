from flask import Flask, render_template

app = Flask(__name__)

# Sample list of items (you can replace this with your own data)
items = ['Item 1', 'Item 2', 'Item 3', 'Item 4', 'Item 5']

@app.route('/items')
def display_items():
    return render_template('items.html', items=items)

if __name__ == '__main__':
    app.run(debug=True)
