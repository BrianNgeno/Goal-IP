from flask import render_template,redirect,url_for,abort,request
from . import main
from flask_login import login_required,current_user
from ..models import User, Pitches,Comments
from .forms import UpdateProfile , PitchForm, CommentForm
from .. import db,photos

#views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data.
    '''

    title = 'Home - Welcome to The Best Pitch Review Website Online'
    pitch = Pitches.query.filter_by(category='technology')
    pitchone = Pitches.query.filter_by(category='misconception')
    pitchtwo = Pitches.query.filter_by(category='disses')
    pitchthree = Pitches.query.filter_by(category='commit_line')
    pitchfour = Pitches.query.filter_by(category='funny')
    pitchfive = Pitches.query.filter_by(category='jokes')
    
    return render_template('index.html', title = title, pitch = pitch,pitchone=pitchone, pitchtwo=pitchtwo, pitchthree=pitchthree, pitchfour=pitchfour, pitchfive=pitchfive)

# Routes for displaying the different pitches
@main.route('/pitch/new',methods=['GET','POST'])
@login_required
def new_pitch():
    form = PitchForm()
    if form.validate_on_submit():
        actual_pitch = form.content.data
        new_pitch = Pitches(actual_pitch=actual_pitch,category = form.category.data,user=current_user)
        new_pitch.save_pitch()
        return redirect(url_for('main.view_pitch'))
    return render_template('pitch.html',form = form)

@main.route('/pitch/new/view')
def view_pitch():
    pitch = Pitches.query.filter_by(category='technology')
    pitchone = Pitches.query.filter_by(category='misconception')
    pitchtwo = Pitches.query.filter_by(category='disses')
    pitchthree = Pitches.query.filter_by(category='commit_line')
    pitchfour = Pitches.query.filter_by(category='funny')
    pitchfive = Pitches.query.filter_by(category='jokes')
    
     

    return render_template('index.html',pitch = pitch,pitchone=pitchone, pitchtwo=pitchtwo, pitchthree=pitchthree, pitchfour=pitchfour, pitchfive=pitchfive)


@main.route('/pitch/new/comment/<int:id>',methods = ['GET','POST'])
@login_required
def new_comment(id):
    form = CommentForm()
    if form.validate_on_submit():
        new_comment = Comments(comment_name = form.comment_name.data,user=current_user, pitches_id =id)
        db.session.commit()
        return redirect(url_for('.index'))
    return render_template('pitch.html',form = form)

@main.route('/pitch/new/comment/<int:id>/view')
def view_comment(id):
    comment = Comments.query.filter_by(pitches_id= id)
    return render_template('comment.html',comment = comment)

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

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    return render_template("profile/profile.html",user=user)