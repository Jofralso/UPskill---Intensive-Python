from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', greeting= 'Hello, Flask with Jinja2!')

if __name__=='__main__':
    app.run()