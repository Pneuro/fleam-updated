from flask import Flask, redirect
from admin.admin import admin
from main.main import main
from db import db, ma
from flask_migrate import Migrate
from fleam_spider.spiders.fleam_spider import spider


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://hwpahxlqhtzioo:4a7d6c43785c6d5f551ea5f0ef3d6157b85655c127aeeda8376a09e1050d845e@ec2-54-224-124-241.compute-1.amazonaws.com:5432/dlfvt18p3ebom'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    app.register_blueprint(main)
    app.register_blueprint(admin)
    app.register_blueprint(spider)
    db.init_app(app)
    with app.app_context():
        migrate = Migrate()
        migrate.init_app(app)
        ma.init_app(app)
        
    return app

app = create_app()






@app.route('/')
def fleam():
    ''' This route shall redirect to the main folder index.html file '''
    return redirect('admin/login')

if __name__ == '__main__':
    app.run()