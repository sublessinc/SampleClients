from flask import Flask, request
from flask.globals import current_app
import testProfile
import json

app = Flask(__name__)

@app.route("/")
def index():
    return current_app.send_static_file("index.html")

@app.route("/profile/TestUser")
def TestUser():
    return testProfile.GenerateUserProfile()

@app.route('/webhook', methods=['POST'])
def creatorStatusWebhook():
    returnedCreator = json.loads(request.data)
    print(returnedCreator)
    print("Creator Email: " + returnedCreator['email'], flush=True)
    print("Creator Username: " + returnedCreator['username'], flush=True)
    print("Creator Status: " + str(returnedCreator['active']), flush=True)
    print("Creator Has been deleted: " + str(returnedCreator['isDeleted']), flush=True)
    print("Creator Subless Id: " + returnedCreator['id'], flush=True)
    return "Ok"

@app.errorhandler(Exception)
def HandleException(e):
    return str(e)