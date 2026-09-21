<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Réinitialiser le mot de passe</title>
</head>
<body>
    <h2>Réinitialiser le mot de passe</h2>
    <form action="reset_password_process.php" method="post">
        <input type="hidden" name="token" value="<?php echo $_GET['token']; ?>">
        <label for="new_password">Nouveau mot de passe :</label><br>
        <input type="password" id="new_password" name="new_password" required><br><br>
        <input type="submit" value="Réinitialiser le mot de passe">
    </form>
</body>
</html>
