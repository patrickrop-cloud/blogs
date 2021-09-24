from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField, SubmitField,TextAreaField,BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from wtforms.validators import Required



class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')     

class BlogForm(FlaskForm):
    title = StringField('Blog title', validators = [Required()])
    content = TextAreaField('Blog content', validators = [Required()])
    submit = SubmitField('Submit')


class CommentForm(FlaskForm):
    title = StringField('Comment title', validators = [Required()])
    comment = TextAreaField('Comment review')
    submit = SubmitField('Submit')

