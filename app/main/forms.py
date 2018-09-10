from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import Required, Email, EqualTo
from ..models import User
from wtforms import ValidationError

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class PitchForm(FlaskForm):
    content = TextAreaField('Your pitch')
    submit = SubmitField('Submit')

class CategoriesForm(FlaskForm):
	name = TextAreaField('Write Comment')
	submit = SubmitField('Submit')