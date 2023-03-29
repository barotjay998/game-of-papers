from flask import Flask
from .api import register_blueprints
from .views import views_bp

def create_app():
    app = Flask(__name__)
    
    # Register blueprints for the API
    register_blueprints(app)

    # Register the views blueprint
    app.register_blueprint(views_bp, url_prefix='')

    return app