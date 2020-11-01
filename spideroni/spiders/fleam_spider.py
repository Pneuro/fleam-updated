import scrapy
from flask import request, g, session, current_app
from models import SearchForm
from db import db, SearchQuery, search_schema, searchs_schema, ma
from app import app

# Offer up, Craigslist, FB letgo


class FleamSpider(scrapy.Spider):
    name = "fleam_spider"
    '''THIS SPIDER TO RECEIVE DATA FROM THE INPUT OF THE FLASK FORM THEORETICALLY FROM DATABASE THAT IT JUST ADDED BEFORE RUNNING'''

    query = db.session.query(SearchQuery.query).order_by(
        SearchQuery.id.desc()).first()
    city = db.session.query(SearchQuery.city).order_by(
        SearchQuery.id.desc()).first()
    max_price = db.session.query(SearchQuery.price).order_by(
        SearchQuery.id.desc()).first()
    #dbq = db.session.query(SearchQuery.city).order_by(SearchQuery.id.desc()).first()

    query.query.replace(' ', '%20')

    # clean up data from db
    query = query.query
    city = city.city
    max_price = max_price.price

    craigsearch = f'https://{city}.craigslist.org/search/sss?query={query}&max_price={max_price}'
    offerup_search = f'https://offerup.com/search/?q={query}'
    # facebook_search = f'https://www.facebook.com/108116349210397/search/?q={query}'
    recycler = f'https://www.recycler.com/search?keyword={query}&location={city}&category='
    hoobly = f'https://www.hoobly.com/search?q={query}'

    # Running tests with these sites first.
    start_urls = [
        craigsearch,
        # offerup_search,
        # hoobly,

    ]

    def parse(self, response):
        # items = FleamscrapeItem()
        custom_settings = {
            'FEED_URI': '/tmp/result.json'
        }
        # dbq = SearchQuery.query.order_by(SearchQuery.id.desc()).first()
        # print(dbq.id)
        # Choose a search engine to acquire data
        scrape_sites = ['cl', 'ou', 'fb', 'hbly']
        # CraigsList Functionality
        for search_engine in scrape_sites:
            if search_engine == 'cl':
                results = response.css('ul.rows')  # Grabbing Craigslist

                for i in results:
                    for r in i.css('li.result-row'):
                        # title = r.css('a.result-title::text').get()
                        # price = r.css('span::text').get()
                        # Link = r.css('a::attr(href)').get()
                        # date_posted = r.css('time.result-date::text').get()
                        # image = r.xpath(
                        #     '/html/body/section/form/div[4]/ul/li[1]/a/div[1]/div/div[1]/img').extract(),
                        # source = 'Craigslist'
                        yield {
                            'title': r.css('a.result-title::text').get(),
                            'price': r.css('span::text').get(),
                            'Link': r.css('a::attr(href)').get(),
                            'date_posted': r.css('time.result-date::text').get(),
                            # 'image': r.css('a.result-img.gallery').get(),
                            # 'source': 'Craigslist'
                        }
            # Offer Up Functionality
            elif search_engine == 'ou':
                result = response.css('div#db-item-list')  # Grabbing Offerup

                for data in result:
                    for data in result.css('a._109rpto'):
                        # for data in r:

                        title = data.css('span._nn5xny4::text').get()
                        price = data.css('span._s3g03e4::text').get()
                        Link = data.css('a::attr(href)').get()
                        date_posted = None
                        image = data.css('img._ipfql6::attr(src)')[
                            1].extract(),
                        source = 'Offer Up'

                        yield {
                            'title': data.css('span._nn5xny4::text').get(),
                            'price': data.css('span._s3g03e4::text').get(),
                            'Link': f'http://www.offerup.com/{Link}',
                            'date_posted': None,
                            'image': image[0],
                            'source': 'Offer Up'
                        }

            elif search_engine == 'hbly':

                results_hbl = response.css(
                    'body > div.container > div > div.col-sm-9.col-md-9.col-lg-9 > table')  # Grabbing Craigslist'
                print(f'This is the thing a thing{results_hbl}')
                for i in results_hbl:

                    yield {
                        'title': r.css('#vGEZ4 > td:nth-child(2) > h4 > a').get(),
                        'price': r.css('span::text').get(),
                        'Link': r.css('a::attr(href)').get(),
                        'date_posted': r.css('time.result-date::text').get(),
                        'image': r.css('a.result-img.gallery').get(),
                        'source': 'Craigslist'
                    }
