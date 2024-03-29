<!DOCTYPE HTML>
<html>
<head>
    <title>Subless PHP sample</title>
    <!-- Load subless2.0.js onto pages with content owned by a particular creator to automatically track a user -->
    <script type="module">
        import { SublessUsingUris } from 'https://app.subless.com/dist/subless2.0.js';
        SublessUsingUris();
    </script></head>
</head>
<body>
Welcome to your profile
<br/>
<?php 
// Define configuration
$username = 'TestUser';
$clientId = 'PARTNER CLIENT ID';
$clientSecret = 'PARTNER CLIENT SECRET';
$sublessPaymentsUrl = 'https://app.subless.com';
$sublessAuthuthUrl = 'https://login.subless.com';
?>

<?php
require __DIR__ . './../vendor/autoload.php';
// Request a client credentials token
$client = new GuzzleHttp\Client();
$authRes = $client->post($sublessAuthuthUrl . '/oauth2/token', [
    'auth' => [$clientId , $clientSecret ],
    'headers' => ['Content-Type' => 'application/x-www-form-urlencoded'],
    'form_params' => [
        'scope' => $sublessPaymentsUrl . '/creator.register',
        'grant_type' => 'client_credentials'
    ]
]);
$json = json_decode((string)$authRes->getBody(), true);
$token = $json['access_token'];



// Request a one time registration link for a given user
$linkRes = $client->post($sublessPaymentsUrl . '/api/Partner/CreatorRegister?username=' . $username, [
    'headers' => ['Authorization' => 'Bearer ' . $token]
]);
$activationCode = $linkRes->getBody();

?>

<!-- Display registration link on profile page -->
<a href="
<?php
//provide a location for the user to return to after registration
$protocol = ((!empty($_SERVER['HTTPS']) && $_SERVER['HTTPS'] != 'off') || $_SERVER['SERVER_PORT'] == 443) ? "https://" : "http://";
$postActivationRedirect = $protocol . $_SERVER['HTTP_HOST'] . $_SERVER['REQUEST_URI'];
echo $sublessPaymentsUrl;
echo "/login?activation=" . $activationCode .'&postActivationRedirect=' . $postActivationRedirect;
//A redirection back to postActivationRedirect will occur after the subless creator profile is completed.
//The redirect will follow the format: [postActivationRedirect]?sublessId=[sublessId]&creatorId=[username]"
?>"
>Click here to activate your subless account</a>
<br/>
<a href='../home'>Return Home</a>
</body>
</html>
