<?php
// Remplir un tableau associatif avec les informations
$personnes = array(
    array("nom" => "ALAMI", "prenom" => "AHMED", "age" => 30),
    array("nom" => "ALAOUI", "prenom" => "FATIMA", "age" => 29),
    array("nom" => "BAGHDADI", "prenom" => "ACHRAF", "age" => 19),
    array("nom" => "BOUSAIDI", "prenom" => "AHLAM", "age" => 20)
);
?>

<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tableau de personnes</title>
    <style>
        table {
            border-collapse: collapse;
            width: 100%;
        }
        th, td {
            border: 1px solid black;
            padding: 8px;
            text-align: left;
        }
    </style>
</head>
<body>
    <h2>Tableau de personnes</h2>
    <table>
        <thead>
            <tr>
                <th>Nom</th>
                <th>Prénom</th>
                <th>Âge</th>
            </tr>
        </thead>
        <tbody>
            <?php
            // Parcourir le tableau associatif et générer les lignes du tableau HTML
            foreach ($personnes as $personne) {
                echo "<tr>";
                echo "<td>" . $personne['nom'] . "</td>";
                echo "<td>" . $personne['prenom'] . "</td>";
                echo "<td>" . $personne['age'] . "</td>";
                echo "</tr>";
            }
            ?>
        </tbody>
    </table>
</body>
</html>
