from flask import render_template,redirect
from . import main
from flask_login import login_required
#views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data.
    '''

    title = 'Home - Welcome to The Best Pitch Review Website Online'
    
    return render_template('index.html', title = title)

