from flask_wtf import FlaskForm 
from wtforms.fields import TextAreaField, SubmitField, StringField, PasswordField
from wtforms.validators import InputRequired, Email, EqualTo 
from flask_wtf.file import FileRequired, FileField, FileAllowed

ALLOWED_FILE = {'PNG', 'JPG', 'png', 'jpg'}

class DestinationForm(FlaskForm):
    name = StringField('Country', validators=[InputRequired()])
    # two validators, one to ensure that their is an input and another to checo if the description meets lenght requirements
    description = TextAreaField('Description', validators=[InputRequired()])
    image = FileField('Cover Image', validators=[FileRequired(message='image cannot be empty'), FileAllowed(ALLOWED_FILE, message='image must be jpg or png')])
    currency = StringField('Currency', validators=[InputRequired()])
    submit = SubmitField("Create")

class CommentForm(FlaskForm):
    text = TextAreaField('Comment', [InputRequired()])
    submit = SubmitField("Create")

class LoginForm(FlaskForm):
    user_name = StringField('User Name', validators=[InputRequired('Enter user name')])
    password = StringField('Password', validators=[InputRequired('Enter user password')])
    submit = SubmitField("Login")

class RegisterForm(FlaskForm):
    user_name = StringField('User Name', validators=[InputRequired('Enter user name')])
    email_id = StringField("Email Address", validators=[Email("Please enter a valid email address")])
    password = StringField('Password', validators=[InputRequired(), EqualTo('confirm', message="Passwords should match")])
    confirm = PasswordField("Confirm Password")
    submit = SubmitField("Register")

class CommentForm(FlaskForm):
    text = TextAreaField('Comment', [InputRequired()])
    submit = SubmitField('Create')