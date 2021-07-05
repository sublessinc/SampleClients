<!DOCTYPE HTML>
<html>
<head>
    <title>Subless PHP sample</title>
    <script src="http://localhost:7070/dist/subless.js"></script>
</head>
<body>
Welcome to your profile
<br/>
<?php 
// Define configuration
$username = 'TestUser2';
$clientId = '3ifutrgss29mug0n26r176u5k3';
$clientSecret = '1m91oc6emnr1r0fh946b6s7bq9q3ujf2ufa4k38oqss7gnqjouag';
$sublessPaymentsUrl = 'http://localhost:4200';
$sublessAuthuthUrl = 'https://subless.auth.us-east-1.amazoncognito.com';
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
$linkRes = $client->post($sublessPaymentsUrl . '/api/Partner/CreatorRegister?username='.$username, [
    'headers' => ['Authorization' => 'Bearer ' . $token]
]);
$activationCode = $linkRes->getBody();

?>

<!-- Display registration link on profile page -->
<a href="
<?php
echo $sublessPaymentsUrl;
echo "/login?activation=";
echo $activationCode; 
?>"
>Click here to activate your subless account</a>
<br/>
<a href='./home'>Return Home</a>
</body>
</html>
