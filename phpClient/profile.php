<!DOCTYPE HTML>
<html>
<head>
    <title>PHP Application</title>
</head>
<body>
<?php
// Display greeting message
require __DIR__ . '/vendor/autoload.php';
echo 'Welcome to your profile';
$client = new GuzzleHttp\Client();
$res = $client->request('GET', 'http://localhost:7070/api/Authorization/settings', [
    'auth' => ['user', 'pass']
]);
echo $res->getStatusCode();
// "200"
echo $res->getHeader('content-type')[0];
// 'application/json; charset=utf8'
echo $res->getBody();
// {"type":"User"...'

?>
<a href='./home'>Home</a>
</body>
</html>