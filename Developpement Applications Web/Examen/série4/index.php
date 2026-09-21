<?php

session_start(); // Démarrage de session

if ( isset($_SESSION['login']) )
{
    header('Location: admin.php');
}

require_once('db.php');

$errorMsg = '';

if (isset($_GET['deco']) && $_GET['deco'] == '1')
{
    session_destroy();
}

if ( isset($_POST['f1']) )
{
    $email = $_POST['email'];
    $password = $_POST['password'];

    // Requête préparée
    $sql = "SELECT * FROM utilisateurs WHERE email = :email AND pass = :password";
    $stm = $con->prepare($sql);
    $stm->bindValue(':email', $email);
    $stm->bindValue(':password', md5($password));
    $stm->execute();
    
    if ( count($stm->fetchAll()) )
    {
        $_SESSION['login'] = true;
        header('Location: admin.php');
    } else {
        $errorMsg = 'Email ou mot de passe incorrecte!';
    }
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
    <?= $errorMsg ?>
    <form action="index.php" method="post">
        Email: <input type="email" name="email" required /> </br>
        Password: <input type="password" name="password" required /> </br>
        <input type="submit" name="f1" value="Se connecter" />
    </form>
    <a href="">Mot de passe oublié?</a>
    <a href="inscription.php">Inscription</a>
</body>
</html>