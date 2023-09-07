''' 
-SQLAlchemy.Model declarative model base class. 
-It sets the table name automatically instead of needing __tablename__.
-SQLAlchemy.session is a session that is scoped to the current Flask application context. 
It is cleaned up after every request.
-SQLAlchemy.metadata and SQLAlchemy.metadatas gives access to each metadata defined in the config.
-SQLAlchemy.engine and SQLAlchemy.engines gives access to each engine defined in the config.
-SQLAlchemy.create_all() creates all tables.
-You must be in an active Flask application context to execute queries and
to access the session and engine.
'''
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
#Criar extensao
db = SQLAlchemy()
#Criar aplicação
app = Flask(__name__)
#Configurar base de dados SQLite, relativamente a instancia da pasta da aplicacao
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
#inicializar a aplicacao com a extensao
db.init_app(app)

#definir modelo de dados
class User(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    
    def __rep__(self):
        return f'<User {self.username}>'
    
with app.app_context():
    db.create_all()