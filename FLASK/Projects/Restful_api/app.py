from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///e_commerce.db'
db = SQLAlchemy(app)
api = Api(app)
jwt = JWTManager(app)

# Import resource classes
from resources.product import ProductResource
from resources.user import UserRegistrationResource, UserLoginResource
from resources.order import OrderResource

# Add resource routes
api.add_resource(ProductResource, '/products/<int:product_id>')
api.add_resource(UserRegistrationResource, '/register')
api.add_resource(UserLoginResource, '/login')
api.add_resource(OrderResource, '/orders/<int:order_id>')

if __name__ == '__main__':
    from app.models import db
    db.create_all()
    app.run(debug=True)
