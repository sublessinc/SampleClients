import requests
import os
from requests.api import head
from requests.auth import HTTPBasicAuth
from flask import render_template

# THESE TWO VALUES will be provided to you as part
# of your subless account. See: readme.md
# You can also use the environment variables
# CLIENT_ID and CLIENT_SECRET
clientId = 'Your client ID'
clientSecret = 'Your client secret'

username = 'TestUser'
sublessPaymentsUrl = 'https://app.subless.com'
sublessAuthUrl = 'https://login.subless.com'

def GetAClientCredentialsToken():
    global clientSecret
    global clientId
    global sublessPaymentsUrl
    global sublessAuthUrl
    if clientId == 'Your client ID':
        clientId = os.getenv("ClientId")
    print(f'ClientId {clientId}', flush=True)

    if clientSecret == 'Your client secret':
        clientSecret = os.getenv("ClientSecret")
    print(f'ClientSecret {clientSecret}', flush=True)

    sublessAuthUrl = os.getenv("issuerUrl")
    if sublessAuthUrl == None:
        sublessAuthUrl = 'https://subless-test.auth.us-east-1.amazoncognito.com'
    print(f'sublessAuthUrl {sublessAuthUrl}', flush=True)

    sublessPaymentsUrl = os.getenv("SublessUrl")
    if sublessPaymentsUrl == None:
        sublessPaymentsUrl = 'https://app.subless.com'

    print(f'sublessPaymentsUrl {sublessPaymentsUrl}', flush=True)

    r = requests.post(sublessAuthUrl + "/oauth2/token",
                      auth=HTTPBasicAuth(clientId, clientSecret),
                      headers={
                          'Content-Type': 'application/x-www-form-urlencoded'},
                      params={
                          'scope': sublessPaymentsUrl + "/creator.register",
                          'grant_type': 'client_credentials'
                      },
                      verify=False  # Do not disable verification on public servers
                      )

    print(f'Auth response {r}', flush=True)

    if (400 == r.status_code):
        raise Exception(
            "SUBLESS ERROR: You've specified an invalid client id or secret while trying to authenticate.")

    token = r.json()["access_token"]
    return token

def RequestOneTimeRegistrationActivationCode(bearerToken, currentUser):
    r = requests.post(sublessPaymentsUrl + "/api/Partner/CreatorRegister?username=" + currentUser,
                      headers={"Authorization": "Bearer " + bearerToken},
                      verify=False  # Do not disable verification on public servers
                      )
    print(f'Client registration response {r}', flush=True)

    activationCode = r.text
    return activationCode


def GenerateOneTimeLink(activationCode):
    protocol = "https://"
    postActivationRedirect = protocol + "localhost:5000/"
    finalLink = sublessPaymentsUrl + "/login?activation=" + activationCode +\
        "&postActivationRedirect=" + postActivationRedirect
    return finalLink


def GenerateUserProfile(usernameOverride):

    username = usernameOverride
    clientCredentialsToken = GetAClientCredentialsToken()
    activationCode = RequestOneTimeRegistrationActivationCode(
        clientCredentialsToken, username)
    userRegistrationLink = GenerateOneTimeLink(activationCode)
    return render_template('profile.html', creator_link=userRegistrationLink)
