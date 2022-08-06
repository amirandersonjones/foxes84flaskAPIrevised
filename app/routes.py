from app import app #import the app variable defined in __init__.py

from flask import render_template

#if your route's job is to display an html page-> it's return values should be a call to render_template
@app.route('/') # decorator says: this is a route of the flask app 'app' with the url endpoint '/'
def home():
    return render_template('index.html')