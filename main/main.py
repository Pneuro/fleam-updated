from flask import Blueprint, render_template, request, redirect, g, current_app
from models import SearchForm
from db import SearchQuery, User, Results, search_schema, searchs_schema, db

import subprocess


main = Blueprint('main', __name__, 
                template_folder='templates', 
                static_folder='static', 
                url_prefix="/home"
                )

class ScrapeControl():
    def get_data():
        '''This runs the subprocess to actuate the scraper. '''
        subprocess.run(['scrapy', 'crawl', 'fleam_spider', '-o', 'result.csv'])
        return 'ran'
    
    
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
        
        #ScrapeControl.get_data()
        # Redirect here to scrape the data.
        return redirect('result')
    return render_template('index.html', form=form)


@main.route('/result')
def result():
    ''' CONSIDER TRYING TO IMPORT THE SCRAPER HERE AND THEN RUN THOSE COMMANDS HERE LIKE A GOOD PROGRAMMER '''
    db_id = db.session.query(SearchQuery.id).order_by(SearchQuery.id.desc()).first()
    db_query = db.session.query(SearchQuery.query).order_by(SearchQuery.id.desc()).first()
    db_city = db.session.query(SearchQuery.city).order_by(SearchQuery.id.desc()).first()
    db_price = db.session.query(SearchQuery.price).order_by(SearchQuery.id.desc()).first()
    ScrapeControl.get_data()
    result = {
        'query':db_query,
        'city': db_city,
        'price': db_price
    }
    return render_template('result.html', result=result)

@main.route('/about')
def about():
    db_id = db.session.query(SearchQuery.id).order_by(SearchQuery.id.desc()).first()
    db_query = db.session.query(SearchQuery.query).order_by(SearchQuery.id.desc()).first()
    db_city = db.session.query(SearchQuery.city).order_by(SearchQuery.id.desc()).first()
    db_price = db.session.query(SearchQuery.price).order_by(SearchQuery.id.desc()).first()
    ScrapeControl.get_data()
    about = {
        'query':db_query,
        'city': db_city,
        'price': db_price
    }
    return render_template('about.html', result=result)
# TODO Take most recent DB entry and run scraper


# DBQ Methods
# 'add_column', 
# 'add_columns', 
# 'add_entity', 
# 'all', 
# 'as_scalar', 
# 'autoflush', 
# 'column_descriptions', 
# 'correlate', 
# 'count', 
# 'cte', 
# 'delete', 
# 'dispatch', 
# 'distinct', 
# 'enable_assertions', 
# 'enable_eagerloads', 
# 'except_', 
# 'except_all',
# 'execution_options', 
# 'exists', 
# 'filter', 
# 'filter_by', 
# 'first', 
# 'first_or_404', 
# 'from_self', 
# 'from_statement', 
# 'get', 
# 'get_execution_options', 
# 'get_or_404', 
# 'group_by', 
# 'having', 
# 'instances', 
# 'intersect', 
# 'intersect_all', 
# 'is_single_entity', 
# 'join', 
# 'label', 
# 'lazy_loaded_from', 
# 'limit', 
# 'logger', 
# 'merge_result', 
# 'offset', 
# 'one', 
# 'one_or_none', 
# 'only_return_tuples', 
# 'options', 
# 'order_by', 
# 'outerjoin', 
# 'paginate', 
# 'params', 
# 'populate_existing', 
# 'prefix_with', 
# 'reset_joinpoint', 
# 'scalar', 
# 'select_entity_from', 
# 'select_from', 
# 'selectable', 
# 'session', 
# 'slice', 
# 'statement', 
# 'subquery', 
# 'suffix_with', 
# 'union', 
# 'union_all', 
# 'update', 
# 'value', 
# 'values', 
# 'whereclause', 
# 'with_entities', 
# 'with_for_update', 
# 'with_hint', 
# 'with_labels', 
# 'with_lockmode', 
# 'with_parent', 
# 'with_polymorphic', 
# 'with_session', 
# 'with_statement_hint', 
# 'with_transformation', 
# 'yield_per'