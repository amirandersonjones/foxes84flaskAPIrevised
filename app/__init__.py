# imports at the top of any necessary modules/files/class/packages/functions - whatever we need from other files for this file to work.

# from the flask package that we installed import the Flask object/class

from flask import Flask

# from our config file import the Config class that we created
from config import Config

# define/instantiate our Flask object...aka tell the computer that this is a flask app
app = Flask(__name__, static_url_path='/static', static_folder='static')

# tell this app how it should be configured. Does it have a database, is it a development or production flask app, does it have passwords or secret keys???- over to the config.py file to set up for this

# aka configure our flask app from the Config object we just wrote
app.config.from_object(Config)

# tell the flask app if any routes or models exist!
# import the routes file here(must be after the definition and config app)
from . import routes