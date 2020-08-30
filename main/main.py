from flask import Blueprint, render_template, request, redirect, g, current_app
from models import SearchForm
from db import db, SearchQuery, User, Results
import subprocess

main = Blueprint('main', __name__, 
                template_folder='templates', 
                static_folder='static', 
                url_prefix="/home"
                )

class ScrapeControl():
    def get_data():
        '''This runs the subprocess to actuate the scraper. '''
        subprocess.run(['scrapy', 'crawl', 'fleam'])
        return
    
    
@main.route('/')
@main.route('/home', methods=['POST', 'GET'])
def index():
    form = SearchForm()
    if request.method == 'POST':
        query = request.form['query'],
        city = request.form['city'],
        price = request.form['price'],
        db_query = SearchQuery(query, city, price)
        db.session.add(db_query)
        db.session.commit()
        print(SearchQuery.city.all_())
        fucker = dir(SearchQuery.city.all_)
        
        for i in fucker:
            print(i)
        # Redirect here to scrape the data.
        return redirect('')
    return render_template('index.html', form=form)


@main.route('/user/<query>')
def show_user(query):
    user = User.query.filter_by(query=query).first_or_404()
    return render_template('show_user.html', user=user)


# TODO Take most recent DB entry and run scraper