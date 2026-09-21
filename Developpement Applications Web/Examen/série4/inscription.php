<?php 

require_once('db.php');

$errorMsg = '';

if ( $_SERVER['REQUEST_METHOD'] == 'POST' )
{
    if ( $_POST['password1'] == $_POST['password2'] )
    {
        $sql = "INSERT INTO utilisateurs(email, pass) VALUES (:email, :password)";
        $stm = $con->prepare($sql);
        $stm->bindValue(':email', $_POST['email']);
        $stm->bindValue(':password', md5($_POST['password1']));
        $stm->execute();

        header('Location: index.php');
    } else {
        $errorMsg = 'Les mots de passe sont différents!';
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
    <form action="" method="post">
        Email: <input type="email" name="email" required /> </br>
        Mot de passe: <input type="password" name="password1" required /> </br>
        Confirmation de mot de passe: <input type="password" name="password2" required /> </br>
        <input type="submit" value="S'inscrire" />
    </form>
</body>
</html>