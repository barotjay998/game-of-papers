from flask import Blueprint, render_template

views_bp = Blueprint('views_bp', __name__, static_folder='static', template_folder='templates')


@views_bp.route('/')
def index():
    return render_template('index.html')

@views_bp.route('/papers')
def papers():
    return render_template('papers.html')

@views_bp.route('/conference')
def conference():
    return render_template('conference.html')

@views_bp.route('/login')
def login():
    return render_template('login.html')