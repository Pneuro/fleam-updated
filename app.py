from flask import Flask, redirect
from admin.admin import admin
from main.main import main
from db import db


app = Flask(__name__)


app.register_blueprint(main)
app.register_blueprint(admin)
db.init_app(app)



@app.route('/')
def fleam():
    ''' This route shall redirect to the main folder index.html file '''
    return redirect('admin/login')

if __name__ == '__main__':
    app.run()