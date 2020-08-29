from flask import Flask, redirect
from admin.admin import admin
from main.main import main
from db import db
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://hwpahxlqhtzioo:4a7d6c43785c6d5f551ea5f0ef3d6157b85655c127aeeda8376a09e1050d845e@ec2-54-224-124-241.compute-1.amazonaws.com:5432/dlfvt18p3ebom'

app.register_blueprint(main)
app.register_blueprint(admin)
db.init_app(app)
migrate = Migrate()
migrate.init_app(app)



@app.route('/')
def fleam():
    ''' This route shall redirect to the main folder index.html file '''
    return redirect('admin/login')

if __name__ == '__main__':
    app.run()