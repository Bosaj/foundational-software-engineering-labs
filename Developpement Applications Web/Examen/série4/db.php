<?php 

$host = 'localhost';
$dbName = 'login103';
$dbUser = 'root';
$dbPassword = '';

try {
    $con = new PDO("mysql:host=$host;dbname=$dbName", $dbUser, $dbPassword);
} catch (PDOException $e) {
    die("Consulter l'administrateur");
    echo $e->getMessage();
}