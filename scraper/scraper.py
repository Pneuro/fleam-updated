from flask import Blueprint, render_template, request, redirect, url_for

scraper = Blueprint('scraper', __name__,
                        template_folder='templates', static_folder='static', url_prefix='/scraper')

@scraper.route('/')
@scraper.route('/scraper', methods=['POST', 'GET'])
def scraper():
    ''' Route to scrape data extracted from data most recently added to DB  '''
    
    if request.method == 'POST':
        print(request)
        return redirect(url_for('main.index'))
    
    return render_template('scraper.html', title='Scraper')