from flask import render_template,redirect,url_for,abort
from . import main
from flask_login import login_required
from ..models import User
from .forms import ReviewForm,UpdateProfile
from .. import db

#views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data.
    '''

    title = 'Home - Welcome to The Best Pitch Review Website Online'
    
    return render_template('index.html', title = title)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)