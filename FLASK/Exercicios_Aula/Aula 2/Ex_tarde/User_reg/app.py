#1- Setup Flask application w/ SQLAlchemy and SQLite database

#MySQL mysql://username:password@hostname/database
#Postgres postgresql://username:password@hostname/database
#SQLite (Unix) sqlite:////absolute/path/to/database
#SQLite (Windows) sqlite:///c:/absolute/path/to/database


from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

#Implemented for step 4
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

app= Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///mydatabase.db'
app.config['SECRET_KEY'] = "random string"
db=SQLAlchemy(app)

#2- Create User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

#4- Implement Form Validation (Flask-WTF) 
class RegistrationForm(FlaskForm):
    username =  StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    submit = SubmitField('Register')

#3- Create a Registration Form
'''
@app.route('/register', methods=['GET', 'POST'])
def register():
    #Form validation Object
    if request.method == 'POST':
        #handle form submission
        username = request.form['username']
        email = request.form['email']
        
        #save user data in the database
        user = User(username=username, email=email)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('registered_users'))
    return render_template('register.html')
'''
#5- Implement form validation
@app.route('/register', methods=['GET', 'POST'])
def register():
    #Form validation Object
    form = RegistrationForm()
    if form.validate_on_submit():
        username= form.username.data
        email = form.email.data
        #save user data in the database
        user = User(username=username, email=email)
        db.session.add(user)
        db.session.commit()
        flash('Registration succesful!','success')
        return redirect(url_for('registered_users'))
    return render_template('register.html', form=form)

#6- Display registered users
@app.route('/users')
def registered_users():
    users=User.query.all()
    return render_template('users.html', users=users)

if __name__ == '__main__':

    with app.app_context():
        db.create_all()
    app.run(debug = True)
