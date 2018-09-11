from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField, SelectField
from wtforms.validators import Required, Email, EqualTo
from ..models import User
from wtforms import ValidationError

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class PitchForm(FlaskForm):
    content = TextAreaField('Your pitch')
    category = SelectField('Category',choices=[('disses','disses'),('technology','technology'),('commit_line','commit_line'),('funny','funny'),('jokes','jokes')])
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):
    comment_name = TextAreaField('Write comment')
    submit = SubmitField('Submit')