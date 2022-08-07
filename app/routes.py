from app import app #import the app variable defined in __init__.py

from flask import render_template

#non-flask imports for route functionality
#import choice for our random behavior
from random import choice
from .services import getEmpireData

#if your route's job is to display an html page-> it's return values should be a call to render_template
@app.route('/') # decorator says: this is a route of the flask app 'app' with the url endpoint '/'
def home():
    x = choice(['Hello Civilizations!', 'Hello Age of Empires Fans!', 'Welcome Insiders!'])
    return render_template('index.html', greet=x)

@app.route('/facts')
def facts():
    title = 'Age of Empires Facts: '
    headline = 'Get your need-to-know facts about Age of Empires Facts!'
    return render_template('facts.html', headline=headline, title=title)

@app.route('/civilizations')
def civilizations():
    empiredata = getEmpireData()
    print(empiredata)
    return render_template('civilizations.html', empiredata=empiredata)