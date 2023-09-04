from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Olá, Flask!"

@app.route('/sobre')
def sobre():
    return "Esta é a página Sobre!"

if __name__ == '__main__':
    app.run()
    
