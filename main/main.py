from flask import Blueprint, render_template, request, redirect, g, current_app
from models import SearchForm
from db import db, SearchQuery, User, Results, search_schema, searchs_schema
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
        
        
        # Redirect here to scrape the data.
        return redirect('result')
    return render_template('index.html', form=form)


@main.route('/result')
def result():
    
    
    
    dbq = db.session.query(SearchQuery.city).first()
    
    return f'{dbq}'


# TODO Take most recent DB entry and run scraper