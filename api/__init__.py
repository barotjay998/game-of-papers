from flask import Flask

app = Flask(__name__)

from api.documents import documents_bp
from api.recommendations import recommendations_bp

app.register_blueprint(documents_bp, url_prefix='/documents')
app.register_blueprint(recommendations_bp, url_prefix='/recommendations')