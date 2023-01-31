from flask import Flask, request, render_template
from flask.globals import current_app

import profile
import json

app = Flask(__name__)

@app.route("/")
def index():
    return current_app.send_static_file("login.html")

@app.route("/profile/<username>")
def TestUser(username):
    return profile.GenerateUserProfile(username)

@app.route("/tagContent/<username>")
def TagContent(username):
    return render_template('tagContent.html', creatorUsername=username)

@app.route("/uriContent/<username>")
def UriContent(username):
    return render_template('uriContent.html', creatorUsername=username)


# To be notified when creators link their account for your site to subless, set up a webhook to recieve a post call.
# Once you've set up and deployed your API, register the URI on your subless partner account page.
@app.route('/webhook', methods=['POST'])
def creatorStatusWebhook():
    # A Json object will be sent with the properties below
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