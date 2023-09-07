from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello():
    return "Olá, Flask!"

@app.route('/sobre')
def sobre():
    return "Esta é a página Sobre!"

@app.route('/saudacao/<nome>')
def saudacao(nome):
    return render_template('saudacao.html', nome=nome)

if __name__ == '__main__':
    app.run(debug=True)
    
