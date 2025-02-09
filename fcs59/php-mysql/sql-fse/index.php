<?php

$db = mysqli_connect('localhost', 'root', '', 'fcs-exam') or die('Error');

$query = 'Select * from blogs';
$result = mysqli_query($db, $query);

?>

<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP</title>
</head>

<body>
    <table>
        <tr>
            <td>ID</td>
            <td>Title</td>
            <td>Author</td>
            <td>Created At</td>
        </tr>
        <tr>
            <?php while ($row = mysqli_fetch_array($result)) { ?>
                <td><?php echo $row['id']; ?></td>
                <td><?php echo $row['title']; ?></td>
                <td><?php echo $row['author']; ?></td>
                <td><?php echo $row['create_at']; ?></td>
            <?php } ?>
        </tr>
    </table>
</body>

</html>