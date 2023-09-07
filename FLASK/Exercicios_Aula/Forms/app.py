from flask import Flask, render_template, request, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] ='your_secret_key'
#Formulario
class MeuFormulario(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    submit = SubmitField('Submit')
    

@app.route('/')
def home():
    return 'Bem-vindo!'

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    form = MeuFormulario()
    #Validacao de formularios e envio
    if form.validate_on_submit():
        
        #mensagens flash
        flash('A sua mensagem foi enviada com sucesso!', 'Success')
        return redirect(url_for('contact'))
    return render_template('contact.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)