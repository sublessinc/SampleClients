from flask import Flask
from flask.globals import current_app
import testProfile

app = Flask(__name__)

@app.route("/")
def index():
    return current_app.send_static_file("index.html")

@app.route("/profile/TestUser")
def TestUser():
    return testProfile.GenerateUserProfile()