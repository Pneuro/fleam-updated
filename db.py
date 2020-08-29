from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey



db = SQLAlchemy()


class SearchQuery(db.Model):
    __tablename__ = 'Queries'
    
    id = db.Column(db.Integer, primary_key=True)
    query = db.Column(db.String())
    city = db.Column(db.String())
    price = db.Column(db.Integer())
    
    def __init__(self, query, city, price):
        self.query = query
        self.city = city
        self.price = price
        
    def __repr__(self):
        return f'<id: {self.id},\n query: {self.query}>'
  
  
class User(db.Model):
    __tablename__ = 'Users'
    
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())
    email = db.Column(db.String())
    password = db.Column(db.String())
    location = db.Column(db.String())
    
    def __init__(self, first_name, last_name, password, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password
        self.location = location
    
    def __repr__(self):
        return f'<id: {self.id} name {self.first_name} {self.last_name}>'
    
    
    
class Results(db.Model):
    __tablename__ = 'Results'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())
    city = db.Column(db.String())
    price = db.Column(db.Integer())
    url = db.Column(db.String())
    date_posted = db.Column(db.String())
    source = db.Column(db.String())
    
    def __init__(self, title, city, price, url, date_posted, source):
        self.title = title
        self.city = city
        self.price = price
        self.url = url
        self.date_posted = date_posted
        self.source = source
        
    def __repr__(self):
        return f'<id: {self.id} Title {self.title},  {self.city}>'