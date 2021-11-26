from flask import render_template
from app import application

@application.route('/')
@application.route('/index')
def index():
    return render_template('index.html', title='CovidPrediction.com')

@application.route('/prediction1')
def exercise1():
    return render_template('prediction1.html', title='Stay Home Notice Guideline Predictor')

@application.route('/prediction2')
def exercise2():
    return render_template('prediction2.html', title='Covid Cases Predictor')