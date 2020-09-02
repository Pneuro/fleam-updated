from flask import Blueprint, render_template, request, redirect, url_for
from models import LoginForm, RegistrationForm

admin = Blueprint('admin', __name__,
                        template_folder='templates', static_folder='static', url_prefix='/admin')

@admin.route('/')
@admin.route('/login', methods=['POST', 'GET'])
def login():
    ''' Route to admin.html  '''
    form = LoginForm()
    if request.method == 'POST':
        if request.form['email']:
            print(request.form['email'])
        print(request)
        return redirect(url_for('main.index'))
    
    return render_template('login.html', title='Login', form=form)



@admin.route('/register', methods=['POST', 'GET'])
def register():
    ''' Route to admin.html  '''
    form = RegistrationForm()
    if request.method == 'POST':
        
        print(request)
        return redirect(url_for('main.index'))
    
    return render_template('register.html', title='Login', form=form)