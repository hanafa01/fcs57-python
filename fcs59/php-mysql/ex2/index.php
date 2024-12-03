<?php 

$db = mysqli_connect('localhost', 'root', '', 'fcs') or die('Error connecting to database');

$query = "Select * From students";
$result = mysqli_query($db, $query);

displayTable($result);

function displayTable($result){
    if(mysqli_num_rows($result) > 0){
        echo '<table>';
        echo '<tr><th>ID</th><th>Name</th><th>Grade</th><th>Subject</th></tr>';
        while($row = mysqli_fetch_assoc($result)){
            echo '<tr>';
            echo "<td>". $row['id'] ."</td>";
            echo "<td>". $row['name'] ."</td>";
            echo "<td>". $row['grade'] ."</td>";
            echo "<td>". $row['subject'] ."</td>";
            echo '</tr>';
        }
        echo '</table>';
    }else{
        echo 'No Students';
    }
}


?>