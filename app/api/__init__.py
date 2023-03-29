from flask import Blueprint
from .documents import documents_bp
from .recommendations import recommendations_bp

def register_blueprints(app):
    app.register_blueprint(documents_bp, url_prefix='/documents')
    app.register_blueprint(recommendations_bp, url_prefix='/recommendations')