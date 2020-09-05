from flask import Flask, redirect, current_app, g, session, request
from admin.admin import admin
from main.main import main
from db import db, ma
from flask_migrate import Migrate
import os

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://hwpahxlqhtzioo:4a7d6c43785c6d5f551ea5f0ef3d6157b85655c127aeeda8376a09e1050d845e@ec2-54-224-124-241.compute-1.amazonaws.com:5432/dlfvt18p3ebom'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.register_blueprint(main)
    app.register_blueprint(admin)
   
    with app.app_context():
        db.init_app(app)
        db.create_all()
        migrate = Migrate()
        migrate.init_app(app)
        ma.init_app(app)
        
    return app

app = create_app()

app.config.update(
    SECRET_KEY=os.urandom(24),

    # Set the session cookie to be secure
    SESSION_COOKIE_SECURE=True,

    # Set the session cookie for our app to a unique name
    SESSION_COOKIE_NAME='Portfolio-WebSession',

    # Set CSRF tokens to be valid for the duration of the session. This assumes you’re using WTF-CSRF protection
    WTF_CSRF_TIME_LIMIT=None,

    # Configure Environment
    FLASK_ENV='production',

    # Debug
    DEBUG=False
)

app.app_context().push()

for i in dir(session):
    print(i)


@app.route('/')
def fleam():
    ''' This route shall redirect to the main folder index.html file '''
    return redirect('admin/login')

if __name__ == '__main__':
    app.run()