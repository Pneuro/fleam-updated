from flask import Blueprint, render_template, request, redirect
from models import SearchForm
from db import db

main = Blueprint('main', __name__, template_folder='templates', static_folder='static', url_prefix="/home")

@main.route('/')
@main.route('/home', methods=['POST', 'GET'])
def index():
    form = SearchForm()
    if request.method == 'POST':
        response = {
            'query': request.form['query'],
            'city': request.form['city'],
            'price': request.form['price'],
        }
        print(response)
        # Redirect here to scrape the data.
        return redirect('')
    return render_template('index.html', form=form)

