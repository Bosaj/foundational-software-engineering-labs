<?php

$nomFichier = 'text.txt';

if (file_exists($nomFichier)) {
    
    $contenu = file_get_contents($nomFichier);
    
    $nombreCaracteres = mb_strlen($contenu);
    
    $nombreMots = str_word_count($contenu, 0);
    
    echo "Le fichier '$nomFichier' contient : " . "<br>";
    echo "- Nombre de caractères : $nombreCaracteres" . "<br>";
    echo "- Nombre de mots : $nombreMots" . PHP_EOL;
} else {
    echo "Le fichier '$nomFichier' n'existe pas.";
}
