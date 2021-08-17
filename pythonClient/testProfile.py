import requests
from requests.api import head
from requests.auth import HTTPBasicAuth
import json

staticHeader = \
"""
<!DOCTYPE HTML>
<html>
<head>
    <title>Subless Python sample</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/oidc-client/1.11.5/oidc-client.js"
        type="text/javascript"></script>
    <script src="https://pay.subless.com/dist/subless.js"></script>
</head>
<body>
Welcome to your profile
<br/>
"""


# THESE TWO VALUES will be provided to you as part
# of your subless account.
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
    html = staticHeader
    clientCredentialsToken = GetAClientCredentialsToken()
    activationCode = RequestOneTimeRegistrationActivationCode(clientCredentialsToken)
    userRegistrationLink = GenerateOneTimeLink(activationCode)
    html += "<br/>"
    html += "<br/>"
    html += userRegistrationLink
    return html