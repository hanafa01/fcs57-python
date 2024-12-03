<?php 

require 'conn.php';

$query1 = 'SELECT * FROM `test`';
$query2 = "SELECT * FROM `employees` where department = 'Sales'";
$query3 = "SELECT * FROM `employees` ORDER BY salary DESC";
$query4 = "SELECT * FROM `employees` ORDER BY salary DESC LIMIT 3";
$query5 = "SELECT count(*) asx ITnbOfEmployees FROM `employees` where department='HR'";
$query6 = "select department,count(*) as nbOfEmpl from employees GROUP BY department";

$result = mysqli_query($db, $query1);

// $result5 = mysqli_query($db, $query5);

// print_r(mysqli_fetch_assoc($result5)['ITnbOfEmployees']);
?>

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <table>
        <tr>
            <th>ID</th>
            <th>First Name</th>
            <th>Last Name</th>
            <th>Department</th>
            <th>Salary</th>
        </tr>
        <?php 
        if(mysqli_num_rows($result) > 0){
        while($row = mysqli_fetch_array($result)){ 
            
            ?>
        <tr>
            <td><?php echo $row['id']; ?></td>
            <td><?php echo $row['first_name']; ?></td>
            <td><?php echo $row['last_name']; ?></td>
            <td><?php echo $row['department']; ?></td>
            <td><?php echo $row['salary']; ?></td>
        </tr>
        <?php }
    }else{
        echo 'nooo';
    } 
    
    ?>
    </table>
</body>
</html>