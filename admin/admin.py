from flask import Blueprint, render_template, request, redirect, url_for, session
from models import LoginForm, RegistrationForm

admin = Blueprint('admin', 
                __name__,
                template_folder='templates', 
                static_folder='static', 
                url_prefix='/admin')

@admin.route('/')
@admin.route('/login', methods=['POST', 'GET'])
def login():
    ''' Route to admin.html  '''
    
    form = LoginForm()
    if request.method == 'POST':
        if request.form['email']:
            user = request.form['email']
            session['user'] = user
            print(session['user'])
            return redirect(url_for('main.index'))
    else:
        return render_template('login.html', title='Login', form=form)



@admin.route('/register', methods=['POST', 'GET'])
def register():

    ''' Route to admin.html  '''
    form = RegistrationForm()
    if request.method == 'POST':
        
        print(request)
        return redirect(url_for('main.index'))
    
    return render_template('register.html', title='Login', form=form)


@admin.route('/logout', methods=['POST', 'GET'])
def logout():
   
    return redirect('login')
    