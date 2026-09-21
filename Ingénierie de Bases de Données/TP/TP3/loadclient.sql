--Créez un script nommé loadclient.sql pour insérer un client dans la table "clients" en mode interactif.
--Le script doit demander à l'utilisateur de saisir les informations du client et les insérer.

ACCEPT code_client CHAR PROMPT 'Please enter the code number:';
ACCEPT nom_client CHAR PROMPT 'Please enter your family name:';
ACCEPT prenom_client CHAR PROMPT 'Please enter your name:';
ACCEPT ville_client CHAR PROMPT 'Please enter your city name:';
ACCEPT email_client CHAR PROMPT 'Please enter your email:';
ACCEPT type_client CHAR PROMPT 'Please enter the department number:';
ACCEPT adresse_client CHAR PROMPT 'Please enter your address:';

INSERT INTO clients (code_client, nom_client, prenom_client, ville_client, email_client, type_client, adresse_client)
VALUES ('&code_client', '&nom_client', '&prenom_client', '&ville_client', '&email_client', '&type_client', '&adresse_client');
