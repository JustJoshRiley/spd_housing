"""This is the file where we initialize our application."""
from flask import Flask
from hoya.config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Visual studio code comes with a linter that might try to
# push this line to the top of the file. Flask is weird,
# and this won't work. Make sure it stays here, and if you're getting errors
# running it, let me know
from hoya.main.routes import main

# This line "registers" our main blueprint, so flask knows what to execute
# when we access localhost
app.register_blueprint(main)
