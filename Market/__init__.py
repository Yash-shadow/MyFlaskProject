from flask import Flask, render_template, redirect, url_for, session

from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from flask_wtf.csrf import CSRFProtect

from flask_bcrypt import Bcrypt
from flask_login import LoginManager




app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:342516@localhost:3307/market'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SECRET_KEY'] = 'your_secrcet_key'
# app.config['WTF_CSRF_SECRET_KEY'] = 'xsdefrtyuilko9i8u765rej'

db = SQLAlchemy(app)
csrf = CSRFProtect(app) # need to change the expire time and try to make the secret key as dynamic 
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"
login_manager.login_message_category= 'info'

from Market import routes
 
with app.app_context():

    db.create_all()
    

    
    





