<?php 

session_start();

if ($_SESSION['login'] != true)
{
    header('Location: index.php');
}

?>
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <h1>Admin</h1>
    <a href="index.php?deco=1">Se déconnecter</a>
</body>
</html>