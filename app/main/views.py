from flask import render_template,redirect,url_for,abort
from . import main
from flask_login import login_required
from ..models import User
from .forms import UpdateProfile , PitchForm
from .. import db,photos

#views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data.
    '''

    title = 'Home - Welcome to The Best Pitch Review Website Online'
    
    return render_template('index.html', title = title)
# Route for adding a new pitch

@main.route('/category/pitch/new/<int:id>', methods=['GET', 'POST'])
@login_required
def new_pitch(id):
    '''
    Function to check Pitches form
    '''
    form = PitchForm()
    category = PitchCategory.query.filter_by(id=id).first()

    if category is None:
        abort(404)

    if form.validate_on_submit():
        actual_pitch = form.content.data
        new_pitch = Pitches(actual_pitch=actual_pitch,
                            user_id=current_user.id, category_id=category.id)
        new_pitch.save_pitch()
        return redirect(url_for('.category', id=category.id))

    return render_template('new_pitch.html', pitch_form=form, category=category)

# Routes for displaying the different pitches
@main.route('/category/new',methods=['GET','POST'])
@login_required
def new_category():
	form = CategoriesForm()
	if form.validate_on_submit():
		name = form.name.data
		new_category = PitchCategory(name=name)
		new_category.save_category()
		return redirect(url_for('.new_category'))
	title = 'New Pitch Category'
	return render_template('new_category.html',categories_form=form)
    
    # route to display different pitches in every category
@main.route('/category/<int:id>')
def category(id):
    '''
    category route function returns a list of pitches in the category chosen
    '''

    category = PitchCategory.query.get(id)
    if category is None:
        abort(404)

    pitches = Pitches.get_pitches(id)
    return render_template('category.html', category=category, pitches=pitches)



@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))