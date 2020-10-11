# Search will scrape multiple online marketplaces for items and return lowest to hightest price.
from __future__ import unicode_literals
from flask_wtf.csrf import CSRFProtect
from werkzeug.middleware.proxy_fix import ProxyFix
import re
from subprocess import Popen, PIPE
import subprocess
import pandas as pd
import csv
import bs4
from bs4 import BeautifulSoup
import requests
import json
import os
import smtplib
from time import sleep
from urllib.request import Request, urlopen
from datetime import datetime, timedelta
from pymongo import MongoClient
from wtforms.validators import DataRequired, Email
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_pymongo import pymongo
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField, IntegerField, FloatField
from flask import Flask, render_template, jsonify, url_for,  flash, redirect, request, flash, jsonify, session, Blueprint

#from .selen import ScraperBot

app = Flask(__name__)
#ui = WebUI(app)

app.permanent_session_lifetime = timedelta(minutes=5)
app.config.update(

    # Set the secret key to a sufficiently random value
    SECRET_KEY=os.urandom(24),

    # Set the session cookie to be secure
    SESSION_COOKIE_SECURE=True,

    # Set the session cookie for our app to a unique name
    SESSION_COOKIE_NAME='Portfolio-WebSession',

    # Set CSRF tokens to be valid for the duration of the session. This assumes you’re using WTF-CSRF protection
    WTF_CSRF_TIME_LIMIT=None,

    # Configure Environment
    # FLASK_ENV='production',

    # Set Flask App
    # FLASK_APP='app.py',

    # Debug
    DEBUG=False

)


### Config ##########################################

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)
date = datetime.utcnow()

######################### Control panel for scraper #######################################

scrape_sites = [('cl', 'Craigslist'),
                ('ou', 'Offerup'),
                ('fb', 'Facebook'),
                ]

class RegisterForm(FlaskForm):
    id = StringField()
    user = StringField(label='Username', validators=[DataRequired()])
    email = StringField(label='Email', validators=[DataRequired()])
    password = SelectField(label='Password', choices=scrape_sites)
    password2 = StringField(label='Password Confirmation',
                            validators=[DataRequired(password)])
    metro = StringField(label='Nearest Metro Area')
    zip_code = IntegerField(label='Zip Code')

    submit = SubmitField(label='Submit')

# input form


class FleamForm(FlaskForm):
    id = StringField()
    search = StringField(default='Lawnmower')
    city = StringField(default='Sandusky')
    selector = SelectField(label='Selector', choices=scrape_sites)
    distance_miles = StringField(default=50)
    max_price = IntegerField(default=500)
    zipcode = IntegerField(default=44870)
    submit = SubmitField(label='Submit')

# DB Creation // Initilization
class SearchQuery(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    search = db.Column(db.String(120), nullable=False)  # Title of search
    city = db.Column(db.String(120), nullable=False)  # Title of search
    selector = db.Column(db.String(120), nullable=False)  # Title of search
    distance = db.Column(db.Float)  # Heighest price to spend
    price = db.Column(db.Float)  # Heighest price to spend
    zip_code = db.Column(db.Integer)

    def __init__(self, search, city, selector, distance, price, zip_code):
        self.search = search
        self.city = city
        self.selector = selector
        self.distance = distance
        self.price = price
        self.zip_code = zip_code

    def __repr__(self):
        return '<SearchQuery %r>' % self.search


class SearchSchema(ma.Schema):
    class Meta:
        fields = ('id',
                  'search',
                  'city',
                  'price',
                  'distance',
                  'zip_code',
                  'selector'
                  )

# Init schema
search_schema = SearchSchema()
searchs_schema = SearchSchema(many=True)

class ScrapeControl():
    def get_data():
        '''This runs the subprocess to actuate the scraper. '''
        subprocess.run(['scrapy', 'crawl', 'fleam',
                        '-o', 'result.csv'])
        return

    def kill_scraper():
        if os.path.exists('result.csv'):
            with open('result.csv',  "w+") as f:
                f.close()
                print('deleted results')

# Front End
# Crawler
# Home Page // Search
@app.route('/', methods=["POST", "GET"])
@app.route('/index', methods=["POST", "GET"])
def index():
    ''' Home Page of FLEAM
        The purpose of this section is to take in form data, send it through the scrapy scraper attached by the hip, and find the things for the user.
    ''' 
    ScrapeControl.kill_scraper()
    form = FleamForm()
    print(f'Index. {date}')
    if request.method == 'POST':

        # handling results from form input
        print(f'Submitted at {date}')
        search_query = {}
        search_query['search'] = form.search.data
        search_query['city'] = form.city.data
        search_query['selector'] = form.selector.data
        search_query['distance'] = form.distance_miles.data
        search_query['price'] = form.max_price.data
        search_query['zip_code'] = form.zipcode.data
        print('after search_query')
        session["scraper"] = search_query['search']

        # cleaning the data for entry into db
        search = search_query['search']
        city = search_query['city']
        selector = search_query['selector']
        distance = search_query['distance']
        price = search_query['price']
        zip_code = search_query['zip_code']
        print(search_query['search'])

        # INSERT THE SEARCH INTO THE DATABASE THEN IT CAN BE RETREIVED BY SCRAPY AND RAN
        new_query = SearchQuery(search, city, selector,
                                distance, price, zip_code)
        db.session.add(new_query)
        db.session.commit()
        # initialize Selenium First (Trial)
        ScrapeControl.get_data()  # Pulls data from Scrapy which includes Craigslist and Offerup
        # sleep(4)
        ############## THIS IS WHERE FACEBOOK LIVES ##########
        #bot = ScraperBot()
        # sleep(5)

        # # Facebook
    #     facebook = bot.get_facebook(search)  # collect html data from facebook
    #     sleep(2)
    #     fbsoup = BeautifulSoup(facebook, features='html.parser')

    #     # # Now the the data is stored in the data base it will start the scraper and collect and display the results.
    #     with open('facescrape.html', 'w') as facescrape:
    #         facescrape.write(fbsoup)

    #     session['scraper'] = search

    #     # Write a FOR loop to iterate over result date right here
    #     # HTML code line 1753
    #     for fb in fbsoup:
    #         fb_item = []
    #       # make this a list full of comma separated values then append each line to csv
    #         # another for loop with the container of the below items
    #         for load in fb.find_all('div', 'fjf4s8hc'):
    #             for i in load.find_all(
    #                     'span', 'oi732d6d ik7dh3pa d2edcug0 qv66sw1b c1et5uql a8c37x1j muag1w35 enqfppq2 jq4qci2q a3bd9o3v knj5qynh oo9gr5id'):
    #                 for j in i:
    #                     data = j.get_text()
    #                     print(f'Data title: = {data}')
    #                     fb_item.append([data])

    #             for h in load.find_all(
    #                     'span', 'oi732d6d ik7dh3pa d2edcug0 qv66sw1b c1et5uql a8c37x1j muag1w35 enqfppq2 a5q79mjw g1cxx5fr lrazzd5p oo9gr5id'):
    #                 for j in i:
    #                     data = j.get_text()
    #                     print(f'Data price: = {data}')
    #                     fb_item.append([data])

    #             for k in load.find_all(
    #                     'a', 'oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 p8dawk7l'):
    #                 for j in i:
    #                     data = j.get_text()
    #                     print(f'Data third: = {data}')
    #                     fb_item.append([data])
    #         print(f'This is result for item fb{fb_item}')
    #         fb_item.clear()

    #    # Append FACEBOOK DATA to RESULT.CSV
    #     with open('result.csv', 'w') as f:

    #         # LetGo
    #         letgo = bot.letgo_getter(search)
    #     # sleep(2)
    #     lgsoup = BeautifulSoup(letgo, features='lxml')
    #     # Returns a bunch of HTML
    #     grid = lgsoup.find('div', {'class': 'sc-fzoyAV givzfL'})
    #     # Iterate over HTML to get Item = [Title, Price, Link]
    #     collection = []
    #     for div in grid.find_all('div', {'class': 'sc-fzqARJ edUkoJ sc-fzoYkl cLtUmm sc-pZaHX hYxXbw'}):
    #         for div_title in div.find_all('p', 'sc-fznYue gkrhoz'):
    #             title = div_title.get_text()
    #             print(title)

    #         for div_location in div.find_all('p', 'sc-fznYue dkOCRO'):
    #             location = div_location.get_text()
    #             print(location)
    #         # title,price,Link,date_posted,image,source,images,files

    #         Link = None
    #         date_posted = None
    #         image = None
    #         source = 'LetGo'
    #         images = None
    #         files = None
    #         price = None
    #         collection.append(
    #             f'{title},{price},{location},{Link},{date_posted},{image},{source}, \n')
    #         print(collection)
    #         with open('result.csv', 'a') as f:
    #             f.writelines(collection)

    #         collection.clear()

    #     # Write a FOR loop to iterate over result date right here
    #     # Close the browser
    #     bot.close_browser()
        print('data created successfully')
        return redirect('result')
    return render_template('index.html', form=form)

@app.route('/result', methods=["POST", "GET"])
def result():
    session = {"scraper": "scraper"}
    if "scraper" in session:

        search_session = session["scraper"]

        print(f'''\n
            From datetime:{date}
            \n ''')
        dbq = SearchQuery.query.order_by(SearchQuery.id.desc()).first()
        query = dbq.search

        download_link = {}
        with open('result.csv', 'r') as scraped:
            response = pd.read_csv(scraped, delimiter=",")

            df = pd.DataFrame(data=response)
            print(f'This is the df variable: {df}')
        return render_template('result.html', tables=[df.to_html(classes='dataframe', index=False, render_links=True, sparsify=True)], titles=df.columns.values, query=query, download_link=download_link)
    else:
        return redirect(url_for('index'))


@app.route("/login")
def login():
    if request.method == "POST":
        user = request.form["nm"]
        session["user"] = user
        return redirect(url_for("index"))
    else:
        if "user" in session:
            return redirect(url_for("login"))


@app.route("/logout")
def logout():
    session.pop("scraper", None)
    return redirect("login")


if __name__ == '__main__':
    app.run() 




