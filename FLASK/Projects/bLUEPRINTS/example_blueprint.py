from flask import Blueprint

example_blueprint=Blueprint('example_blueprint', __name__)

@example_blueprint.route('/')
def index():
    return 'Isto é uma aplicação exemplo'