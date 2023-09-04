# Aula: Introdução ao Flask e Manipulação de Formulários
## Horas 1-4: Introdução ao Flask

### **Visão Geral do Flask**

- Flask é um framework web leve e versátil para Python.
- Foi projetado para tornar o desenvolvimento web simples e direto.
- O Flask fornece ferramentas essenciais para a construção de aplicações web, incluindo roteamento, templates e muito mais.

### **Instalação e Configuração**

- Antes de começarmos a usar o Flask, é necessário instalá-lo.
- Recomendamos criar um ambiente virtual para seus projetos Flask, a fim de gerenciar as dependências.
- Instale o Flask usando o pip:

```bash
pip install Flask
```

- Crie um novo diretório para o seu projeto Flask.

### **Criação de uma Aplicação Flask Básica**

- Vamos criar uma aplicação simples que exibe "Olá, Flask!".

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Olá, Flask!"

if __name__ == '__main__':
    app.run()
```

- Neste exemplo, importamos o Flask, criamos uma aplicação Flask e definimos uma rota ('/') que retorna "Olá, Flask!" quando acessada.

### **Roteamento e Manipulação de URLs**

- O Flask utiliza rotas para mapear URLs para funções de visualização.
- As rotas são definidas usando o decorador `@app.route`.

```python
@app.route('/sobre')
def sobre():
    return "Esta é a página Sobre."
```

- Neste exemplo, ao acessar `/sobre`, a função `sobre` será acionada e exibirá "Esta é a página Sobre."

### **Templates do Flask**

- O Flask utiliza templates Jinja2 para renderizar HTML.
- Crie um diretório `templates` em sua pasta de projeto para armazenar os templates HTML.
- Renderize templates usando `render_template` do Flask.

```python
from flask import render_template

@app.route('/saudacao/<nome>')
def saudacao(nome):
    return render_template('saudacao.html', nome=nome)
```

- Neste exemplo, passamos a variável `nome` para o template `saudacao.html`.

## Horas 5-8: Manipulação de Formulários e Entrada do Usuário

### **Criação de Formulários com Flask-WTF**

- Flask-WTF é uma extensão que simplifica a manipulação de formulários no Flask.
- Instale-o usando o pip:

```bash
pip install Flask-WTF
```

- Crie um formulário usando Flask-WTF:

```python
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class MeuFormulario(FlaskForm):
    nome = StringField('Nome', validators=[DataRequired()])
    enviar = SubmitField('Enviar')
```

- Adicione o formulário a uma rota e renderize-o em seu template.

### **Validação de Formulários e Envio**

- Utilize a validação de formulários para garantir a correção dos dados.
- Manipule envios de formulários usando requisições POST.

```python
@app.route('/contato', methods=['GET', 'POST'])
def contato():
    formulario = MeuFormulario()
    if formulario.validate_on_submit():
        # Processe os dados do formulário aqui
        nome = formulario.nome.data
        flash(f'Obrigado por entrar em contato, {nome}!', 'success')
    return render_template('contato.html', formulario=formulario)
```

- Neste exemplo, tratamos o envio do formulário, processamos os dados e exibimos uma mensagem de sucesso.

### **Mensagens Flash**

- Mensagens flash fornecem feedback ao usuário.
- Use `flash` para exibir mensagens após o envio do formulário.

```python
from flask import flash

flash('Esta é uma mensagem flash', 'info')
```

- Inclua mensagens `flash` em seu template para notificar os usuários sobre o resultado do envio do formulário.

---
