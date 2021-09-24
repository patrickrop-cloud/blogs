from flask_wtf import FlaskForm
from wtforms import SelectField,SubmitField,PasswordField
from wtforms.validators import Required,Email,EqualTo
from wtforms import ValidationError
# from ..models import User
from wtforms import StringField,BooleanField,PasswordField,SubmitField

class RegistrationForm(FlaskForm):
    email = StringField('Your Email Address',validators=[Required(),Email()])
    username = StringField('Enter your username',validators=[Required()])
    password = PasswordField('Password',validators=[Required(), EqualTo('password_cornfirm',message='Passwords must match')])
    password_confirm = PasswordField('Confirm Passwords',validators=[Required()])
    submit = SubmitField('Sign Up')

    def validate_email(self, data_field):
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError('There is an existing account with this email')

    def validate(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('The user name entered is already taken')

class LoginForm(FlaskForm):
    email = StringField('Enter your Email Adress',validators=[Required(),Email()])
    password = PasswordField('Password',validators=[Required()])
    remember = BooleanField('Remember Me') 
    submit = SubmitField('Sign In')       






