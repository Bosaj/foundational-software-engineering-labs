<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TP N° 1</title>
</head>
<body>
    <h2>Affichage des entiers de 1 à 10 avec PHP</h2>

    <?php
    function afficherEntiers($max) {
        for ($i = 1; $i <= $max; $i++) {
            echo $i . "<br>";
        }
    }
    ?>

    <h3>Affichage avec une boucle while :</h3>
    <?php
    $i = 1;
    while ($i <= 10) {
        echo $i . "<br>";
        $i++;
    }
    ?>

    <h3>Affichage avec une boucle for :</h3>
    <?php
    for ($i = 1; $i <= 10; $i++) {
        echo $i . "<br>";
    }
    ?>

    <h3>Affichage en utilisant une fonction :</h3>
    <?php
    afficherEntiers(10);
    ?>

    <h3>Affichage jusqu'à un nombre quelconque (par exemple, 16) :</h3>
    <?php
    afficherEntiers(16);
    ?>
</body>
</html>