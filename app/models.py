from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_secure = db.Column(db.String(255))
    password_hash = db.Column(db.String(255))
    pitches = db.relationship("Pitches", backref="user", lazy="dynamic")
    comment = db.relationship("Comments", backref="user", lazy="dynamic")



    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.password_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.password_secure,password)
    def __repr__(self):
        return f'User {self.username}'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")


    def __repr__(self):
        return f'User {self.name}'


# class PitchCategory(db.Model):
#     '''
#     Category class define category per pitch
#     '''
#     __tablename__ = 'pitch_categories'
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(255))
#     description = db.Column(db.String(255))


#     # save pitches
#     def save_category(self):
#         '''
#         Function that saves a category
#         '''
#         db.session.add(self)
#         db.session.commit()

#     #get pitch category
#     @classmethod
#     def get_categories(cls):
#         '''
#         Function that returns all the data from the categories after being queried
#         '''
#         categories = PitchCategory.query.all()
#         return categories



class Pitches(db.Model):

    '''
    Defines or creates table in db or Class with instance of all the pitches in the different categories
    '''
    all_pitches = []

    __tablename__ = 'pitches'

    id = db.Column(db.Integer, primary_key=True)
    actual_pitch = db.Column(db.String)
    date_posted = db.Column(db.DateTime, default=datetime.now)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    category = db.Column(db.String)
    comment = db.relationship("Comments", backref="pitches", lazy="dynamic")
    upvote = db.Column(db.Integer)
    downvote = db.Column(db.Integer)
    
    def save_pitch(self):
        '''
        Function to save a pitch
        '''
        db.session.add(self)
        db.session.commit()

    @classmethod
    def clear_pitches(cls):
        '''
        Function that clears all the pitches in a particular category
        '''
        Pitches.all_pitches.clear()

    # display pitches
    @classmethod
    def get_pitches(cls, id):
        '''
        Function that gets a particular pitch when requested by date posted
        '''
        pitches = Pitches.query.order_by(Pitches.date_posted.desc()).filter_by(category_id=id).all()
        return pitches

class Comments(db.Model):
    '''
    Comment class that creates instances of Comments class that will be attached to a particular pi
    '''
    __tablename__ = 'comment'

    # add columns
    id = db.Column(db. Integer, primary_key=True)
    comment_id = db.Column(db.String(255))
    date_posted = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    pitches_id = db.Column(db.Integer, db.ForeignKey("pitches.id"))

    def save_comment(self):
        '''
        Save the comments per pitch
        '''
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(self, id):
        comment = Comments.query.order_by(
            Comments.date_posted.desc()).filter_by(pitches_id=id).all()
        return comment
