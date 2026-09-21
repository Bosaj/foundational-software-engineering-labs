<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TP N° 2 : HTML & CSS & PHP</title>
    <style>
        table {
            border-collapse: collapse;
            width: 50%;
            margin: 20px auto;
        }
        th, td {
            border: 1px solid black;
            padding: 8px;
            text-align: center;
        }
    </style>
</head>
<body>
    <?php
        $villes = array("OUJDA", "NADOR", "BERKANE", "JERADA");
    ?>

    <!-- Liste ul li contenant des liens -->
    <h2>Liste ul li contenant des liens</h2>
    <ul>
        <?php foreach ($villes as $ville): ?>
            <li><a href="#"><?php echo $ville; ?></a></li>
        <?php endforeach; ?>
    </ul>

    <!-- Liste déroulante (select) -->
    <h2>Liste déroulante (select)</h2>
    <select>
        <?php foreach ($villes as $ville): ?>
            <option value="<?php echo $ville; ?>"><?php echo $ville; ?></option>
        <?php endforeach; ?>
    </select>

    <!-- Cases à cocher (checkbox) -->
    <h2>Cases à cocher (checkbox)</h2>
    <form>
        <?php foreach ($villes as $ville): ?>
            <input type="checkbox" id="<?php echo $ville; ?>" name="<?php echo $ville; ?>">
            <label for="<?php echo $ville; ?>"><?php echo $ville; ?></label><br>
        <?php endforeach; ?>
    </form>

    <!-- Boutons radio -->
    <h2>Boutons radio</h2>
    <form>
        <?php foreach ($villes as $ville): ?>
            <input type="radio" id="<?php echo $ville; ?>" name="ville" value="<?php echo $ville; ?>">
            <label for="<?php echo $ville; ?>"><?php echo $ville; ?></label><br>
        <?php endforeach; ?>
    </form>
</body>
</html>
