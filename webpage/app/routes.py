from app import application
from flask import render_template, flash, redirect, url_for
from app.forms import LoginForm, RegistrationForm 
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User 
from werkzeug.urls import url_parse
from app import db
from flask import request 
from app.serverlibrary import * 

@application.route('/')
@application.route('/index')
def index():
	return render_template('index.html', title='Home')

# write down your handler for the routes here

@application.route('/prediction')
def prediction():
	return render_template('prediction.html', title='Task 2')