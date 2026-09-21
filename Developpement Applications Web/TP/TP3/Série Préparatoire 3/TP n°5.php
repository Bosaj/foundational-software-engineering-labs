<?php

$nomFichier = 'nombres.txt';

$handle = fopen($nomFichier, 'w');

if ($handle) {
    
    for ($i = 1; $i <= 1000; $i++) {
        fwrite($handle, $i . PHP_EOL);
    }
    fclose($handle);
    echo "Le fichier {$nomFichier} a été créé et rempli avec succès.";
}
?>