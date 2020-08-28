from flask import Blueprint, render_template
from models import SearchForm

main = Blueprint('main', __name__, template_folder='templates', static_folder='static', url_prefix="/home")

@main.route('/')
@main.route('/home')
def index():
    form = SearchForm()
    return render_template('index.html', form=form)
