from flask_restful import Resource, reqparse
from app.models import Product

class ProductResource(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True, help='Name of the product')
    parser.add_argument('description', type=str, required=False, help='Description of the product')
    parser.add_argument('price', type=float, required=True, help='Price of the product')

    def get(self, product_id):
        # Retrieve a product by ID and return it as JSON
        pass

    def put(self, product_id):
        # Update a product by ID and return the updated product as JSON
        pass

    def delete(self, product_id):
        # Delete a product by ID and return a success message
        pass

    def post(self):
        # Create a new product and return it as JSON
        pass
