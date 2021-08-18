import requests
from requests.api import head
from requests.auth import HTTPBasicAuth
from flask import render_template

# THESE TWO VALUES will be provided to you as part
# of your subless account. See: readme.md
clientId = 'Your client ID';
clientSecret = 'Your client secret';


username = 'TestUser';
sublessPaymentsUrl = 'https://pay.subless.com';
sublessAuthUrl = 'https://subless-test.auth.us-east-1.amazoncognito.com';

def GetAClientCredentialsToken():
    # Request a client credentials token
    r = requests.post(sublessAuthUrl + "/oauth2/token",\
        auth = HTTPBasicAuth(clientId, clientSecret),
        headers = {'Content-Type' : 'application/x-www-form-urlencoded'},
        params = {
                'scope' : sublessPaymentsUrl + "/creator.register",
                'grant_type' : 'client_credentials'
        }
    )

    if (400 == r.status_code):
        raise Exception("SUBLESS ERROR: You've specified an invalid client id or secret while trying to authenticate.")

    token = r.json()["access_token"]
    return token

def RequestOneTimeRegistrationActivationCode(bearerToken):
    r = requests.post(sublessPaymentsUrl + "/api/Partner/CreatorRegister?username=" + username,
        headers = {"Authorization" : "Bearer " + bearerToken}
    )

    activationCode = r.text
    return activationCode

def GenerateOneTimeLink(activationCode):
    protocol = "http://"
    postActivationRedirect = protocol + "localhost:5000/"
    finalLink = sublessPaymentsUrl + "/login?activation=" + activationCode +\
        "&postActivationRedirect=" + postActivationRedirect
    return finalLink

def GenerateUserProfile():
    clientCredentialsToken = GetAClientCredentialsToken()
    activationCode = RequestOneTimeRegistrationActivationCode(clientCredentialsToken)
    userRegistrationLink = GenerateOneTimeLink(activationCode)
    return render_template('profile.html', creator_link=userRegistrationLink)