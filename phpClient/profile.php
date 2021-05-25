<!DOCTYPE HTML>
<html>
<head>
    <title>Subless PHP sample</title>
</head>
<body>
Welcome to your profile
<br/>
<?php 
// Define configuration
$username = 'TestUser';
$clientId = 'PARTNER CLIENT ID';
$clientSecret = 'PARTNER CLIENT SECRET'
$sublessPaymentsUrl = 'https://pay.subless.com';
$sublessAuthuthUrl = 'https://subless.auth.us-east-1.amazoncognito.com';
?>

<?php
require __DIR__ . '/vendor/autoload.php';
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
$linkRes = $client->get($sublessPaymentsUrl . '/api/Partner?username='.$username, [
    'headers' => ['Authorization' => 'Bearer ' . $token]
]);
$activationCode = $linkRes->getBody();

?>

<!-- Display registration link on profile page -->
<a href="
<?php
echo $sublessPaymentsUrl;
echo "?activation=";
echo $activationCode; 
?>"
>Click here to activate your subless account</a>
<br/>
<a href='./home'>Return Home</a>
</body>
</html>