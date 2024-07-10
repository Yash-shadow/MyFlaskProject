from flask_wtf import FlaskForm
from wtforms  import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, ValidationError, DataRequired
from Market.models import User


# Define a simple form 
class MyForm(FlaskForm):
    name = StringField('Name')
    submit = SubmitField('Submit')



class RegistrationForm(FlaskForm):

    def validate_username(self, username):
        user = User.query.filter_by(username=username).first()
        if user:
            raise ValidationError("Username already exists")



    username = StringField(label = 'User Name',validators=[Length(min=2,max=30)]     )
    email_address = StringField(label = 'Email Address',validators=[Email()])
    password = PasswordField(label = 'Password')
    password_confirmation = PasswordField(label = 'Password Confirmation',validators= [EqualTo('password')])
    submit = SubmitField(label = 'Submit')
                         

class LoginForm(FlaskForm):

    # def validate_username(self, username):
    #     user = User.query.filter_by(username=username).first()
    #     if user is None:
    #         raise ValidationError("Username doesn't exist")



    username = StringField(label = 'User Name',validators=[DataRequired()])
    password = PasswordField(label = 'Password',validators=[DataRequired()])
  
    submit = SubmitField(label = 'Login')

   