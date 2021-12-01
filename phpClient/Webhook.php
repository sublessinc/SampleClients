<?php

// To be notified when creators link their account for your site to subless, set up a webhook to recieve a post call.
// Once you've set up and deployed your API, register the URI on your subless partner account page.
if($_SERVER["REQUEST_METHOD"] == "POST")
{
    // A Json object will be sent with the properties below
    $userData = json_decode(file_get_contents("php://input"),true);
    error_log(json_encode($userData) . "\n", 3, "./php.log");
    error_log("Creator Email: " . $userData["email"]  . "\n", 3, "./php.log");
    error_log("Creator Username: " . $userData["username"]  . "\n", 3, "./php.log");
    error_log("Creator Status: " . strval($userData["active"])  . "\n", 3, "./php.log");
    error_log("Creator Has been deleted: " . strval($userData["isDeleted"])  . "\n", 3, "./php.log");
    error_log("Creator Subless Id: " . $userData["id"]  . "\n", 3, "./php.log");
}
?>