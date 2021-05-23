#PHP Client
This example demonstrates both the process for pushing user activity back to subless as they visit creators, and the process for registering creator accounts to subless accounts

## Prerequisites 
* Apache or other webserver
* php7+
* Composer 2+

## Usage
* Place the contents of the sample client folder into your webroot
* navigate to that root, and run
	php composer install
* open profile.php in your preferred text editor
* populate the following with the client id and client secret provided directly to you by subless
	$clientId
	$clientSecret
* browse to home.php


## Home.php
home.php simply loads in the contents of subless.js. That will trigger a login, and once logged in, will call the "hit" api on each page load with the user's token. This allows subless to payout to each creator accessed by said user

## Profile.php
profile.php first requests an access token from the authorization server, then uses that to request a registration link for the user defined by the username variable