<?php
$mysqli = new mysqli('localhost', 'root', '', 'test');

if (isset($_GET["gender"]) && $_GET["gender"] >= 0 && $_GET["gender"] <= 2) {
    $gender = $_GET["gender"];
    $query = $mysqli->prepare("Select * FROM users WHERE gender = ?");
    $query->bind_param("i", $gender);
} else {
    $query = $mysqli->prepare("Select * FROM users;");
}

$query->execute();
$array = $query->get_result();

$array_response = [];
while ($user = $array->fetch_assoc()) {
    $array_response[] = $user;
}

echo json_encode($array_response);


?>


<?php
include("../db_connection/db_info.php");
$date_time =  date("y-m-d h:i");

if (isset($_POST["sender_id"])) {
    $sender_id = $_POST["sender_id"];
} else {
    die("Don't try to mess around bro ;)");
}

if (isset($_POST["receiver_id"])) {
    $receiver_id = $_POST["receiver_id"];
} else {
    die("Don't try to mess around bro ;)");
}

if (isset($_POST["content"])) {
    $content = $_POST["content"];
} else {
    die("Don't try to mess around bro ;)");
}

$is_read = 0;
$query = $mysqli->prepare("INSERT INTO messages (sender_id, receiver_id, content, is_read, date_time) VALUES (?, ?, ?, ?, ?)");
$query->bind_param("iisis", $sender_id, $receiver_id, $content, $is_read, $date_time);
$query->execute();

$array_response = [];
$array_response["message"] = "Message has been successfully sent";
echo json_encode($array_response);

?>