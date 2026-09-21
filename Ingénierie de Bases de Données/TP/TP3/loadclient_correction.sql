ACCEPT code_client PROMPT 'Saisisez le code du client '
ACCEPT nom_client PROMPT 'Saisisez le nom du client '
ACCEPT prenom_client PROMPT 'Saisisez le prenom du client '
ACCEPT ville_client PROMPT 'Saisisez la ville du client '
ACCEPT email_client PROMPT "Saisisez l'email du client "
ACCEPT type_client PROMPT 'Saisisez le type du client '
ACCEPT adresse_client PROMPT 'Saisisez le type du client '


INSERT INTO	clients VALUES ('&code_client', '&nom_client', '&prenom_client','ville_client', '&email_client','&type_client', '&adresse_client' );


