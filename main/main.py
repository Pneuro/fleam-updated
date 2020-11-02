from flask import Blueprint, render_template, request, redirect, g, current_app, session, url_for, abort
from models import SearchForm
from db import SearchQuery, User, Results, search_schema, searchs_schema, db
import pandas as pd
import os
from time import sleep
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

    def kill_scraper():
        if os.path.exists('result.csv'):
            with open('result.csv',  "w+") as f:
                f.close()
                print('deleted results')


@main.route('/')
@main.route('/home', methods=['POST', 'GET'])
def index():
    ScrapeControl.kill_scraper()
    form = SearchForm()
    if request.method == 'POST':
        query = request.form['query'],
        city = request.form['city'],
        price = request.form['price'],
        db_query = SearchQuery(query, city, price)
        db.session.add(db_query)
        db.session.commit()
        ScrapeControl.get_data()
        sleep(2)
        # Redirect here to scrape the data.
        return redirect(url_for('main.result'))
    return render_template('index.html', form=form)


@main.route('/result')
def result():
    error = None
    # Pull items from database
    db_id = db.session.query(SearchQuery.id).order_by(
        SearchQuery.id.desc()).first(),
    db_query = db.session.query(SearchQuery.query).order_by(
        SearchQuery.id.desc()).first(),
    db_city = db.session.query(SearchQuery.city).order_by(
        SearchQuery.id.desc()).first(),
    db_price = db.session.query(SearchQuery.price).order_by(
        SearchQuery.id.desc()).first(),
    city_name = db.session.query(SearchQuery.city).order_by(
        SearchQuery.id.desc()).first()

    # cleaning up data. This chooses the first item in database response.
    id = db_id
    query = db_query[0]
    city = db_city[0]
    price = db_price[0]

    # Converts tuple to((query, )) to 'query'
    query = query.query
    city = city.city
    price = price.price

    if 'result.csv':
        with open('result.csv', 'r') as scraped:
            response = pd.read_csv(scraped, delimiter=",")

            df = pd.DataFrame(data=response)
            #print(f'This is the df variable: {df}')
        return render_template('result.html', tables=[df.to_html(classes='dataframe',
                                                                 index=False,
                                                                 render_links=True,
                                                                 sparsify=True)],
                               titles=df.columns.values,
                               query=query,
                               city=city
                               )
    else:
        abort(500)
        return redirect(url_for('main.index'))


@main.route('/about')
def about():
    return render_template('about.html')


