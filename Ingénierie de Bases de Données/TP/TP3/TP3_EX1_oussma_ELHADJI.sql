--1. Insérer les données suivantes :
INSERT ALL 
   INTO fournisseurs (code_fournisseur, nom_fournisseur) VALUES ('F01', 'Les stylos reunis')
   INTO fournisseurs (code_fournisseur, nom_fournisseur) VALUES ('F02', 'Sarl Ali')
   INTO fournisseurs (code_fournisseur, nom_fournisseur) VALUES ('F03', 'electrolamp')
SELECT * FROM dual;

	COMMIT;

INSERT ALL
	INTO categories(code_categorie, libelle_categorie)
		VALUES	('C01', 'informatique')
	INTO categories(code_categorie, libelle_categorie)
		VALUES	('C02', 'Fournitures de bureau')
	INTO categories(code_categorie, libelle_categorie)
		VALUES('C03', 'Electronique')
SELECT * FROM dual;

INSERT ALL
	INTO articles(code_article, libelle_article, poids_article, couleur_article,prix_vente, prix_achat, stock)
		VALUES	('A01', 'Agrafeuse', 150, 'rouge', 150, 100, 10)
	INTO articles(code_article, libelle_article, poids_article, couleur_article,prix_vente, prix_achat, stock)
		VALUES	('A02', 'Calculatrice', 150, 'Noir', 200, 200, 100)
	INTO articles(code_article, libelle_article, poids_article, couleur_article,prix_vente, prix_achat, stock)
		VALUES	('A03', 'Cachet dateur', 100, 'Blanc', 300, 150, 30)
	INTO articles(code_article, libelle_article, poids_article, couleur_article,prix_vente, prix_achat, stock)
		VALUES	('A04', 'Lampe1', 550, 'Rouge', 149, 105, 30)
	INTO articles(code_article, libelle_article, poids_article, couleur_article,prix_vente, prix_achat, stock)
		VALUES	('A05', 'Lampe2', 550, 'Blanc', 149, 105, 10)
	INTO articles(code_article, libelle_article, poids_article, couleur_article,prix_vente, prix_achat, stock)
		VALUES	('A06', 'Lampe3', 550, 'Bleu', 149, 105, 50)
	INTO articles(code_article, libelle_article, poids_article, couleur_article,prix_vente, prix_achat, stock)
		VALUES	('A07', 'Clavier sans fil', 500.0, 'Noir', 700, 400, 15)
	INTO articles(code_article, libelle_article, poids_article, couleur_article,prix_vente, prix_achat, stock)
		VALUES	('A08', 'Casque audio', 140, 'Vert', 280, 230, 15)
	INTO articles(code_article, libelle_article, poids_article, couleur_article,prix_vente, prix_achat, stock)
		VALUES	('A09', 'Crayon', 20.0, 'rouge', 3, 1, 200)
	INTO articles(code_article, libelle_article, poids_article, couleur_article,prix_vente, prix_achat, stock)
		VALUES	('A10', 'Crayon luxe', 20.0, 'rouge', 6, 3, 190)
SELECT * FROM dual;

	COMMIT;
	
-- Drop the existing check constraint
ALTER TABLE clients DROP CONSTRAINT check_type_client;

-- Add a new check constraint with the updated values
ALTER TABLE clients
ADD CONSTRAINT check_type_client
CHECK (type_client IN ('particulier', 'administration', 'grand compte', 'pme', 'entreprise'));


--2.Créez un script nommé loadclient.sql pour insérer un client dans la table "clients" en mode interactif. Le script doit demander à l'utilisateur de saisir les informations du client et les insérer 
@C:\Users\ousso\Desktop\loadclient.sql


--3. Insérez les 4 premières lignes des données d’exemple suivant dans la table "clients" en exécutant le script que vous avez créé.
-- Execute the script for CL01 with full path
Please enter the code number: CL01
Please enter your family name: El Amrani
Please enter your name: Fatima
Please enter your city name: Rabat
Please enter your email: f.elamrani@gmail.com
Please enter the department number: Particulier
Please enter your address: 15 Avenue Hassan II
--Etc...


-- 4. Pour chaque client créer une commande avec des articles existants.

-- Client CL01
-- Créer une commande pour le client CL01 avec quelques articles existants
INSERT INTO commandes (code_commande, code_client)
VALUES ('CMD001C1', 'CL01');

-- Ajouter des lignes de commande pour la commande CMD001C1 avec des articles existants
INSERT INTO details_commande (code_commande, code_article, quantite)
SELECT 'CMD001C1', 'A01', 2 FROM dual
UNION ALL
SELECT 'CMD001C1', 'A03', 1 FROM dual;

-- Client CL02
-- Créer une commande pour le client CL02 avec quelques articles existants
INSERT INTO commandes (code_commande, code_client)
VALUES ('CMD002C2', 'CL02');

-- Ajouter des lignes de commande pour la commande CMD002C2 avec des articles existants
INSERT INTO details_commande (code_commande, code_article, quantite)
SELECT 'CMD002C2', 'A02', 3 FROM dual
UNION ALL
SELECT 'CMD002C2', 'A04', 2 FROM dual;

-- Client CL03
-- Créer une commande pour le client CL03 avec quelques articles existants
INSERT INTO commandes (code_commande, code_client)
VALUES ('CMD003C3', 'CL03');

-- Ajouter des lignes de commande pour la commande CMD003C3 avec des articles existants
INSERT INTO details_commande (code_commande, code_article, quantite)
SELECT 'CMD003C3', 'A06', 1 FROM dual
UNION ALL
SELECT 'CMD003C3', 'A08', 2 FROM dual;

-- Client CL04
-- Créer une commande pour le client CL04 avec quelques articles existants
INSERT INTO commandes (code_commande, code_client)
VALUES ('CMD004C4', 'CL04');

-- Ajouter des lignes de commande pour la commande CMD004C4 avec des articles existants
INSERT INTO details_commande (code_commande, code_article, quantite)
SELECT 'CMD004C4', 'A09', 5 FROM dual
UNION ALL
SELECT 'CMD004C4', 'A10', 3 FROM dual;

-- 5. Vérifiez vos ajouts.

-- Vérifier les commandes pour chaque client
SELECT * FROM commandes;

-- Vérifier les lignes de commande pour chaque commande
SELECT * FROM details_commande;

-- 6. Validez la transaction

-- Valider la transaction pour tous les clients et commandes
COMMIT;

-- Vérifier les changements après la validation de la transaction
-- (Re-exécuter les requêtes de vérification ci-dessus)

-- Mise à jour et suppression de données :

-- 7. Remplacer l’email du client numéro CL03 par a.oubaha@gmail.com
UPDATE clients
SET email_client = 'a.oubaha@gmail.com'
WHERE code_client = 'CL03';

-- 8. Augmenter le prix de vente de l’article ‘A02’ à 235.
UPDATE articles
SET prix_vente = 235
WHERE code_article = 'A02';

-- 9. Modifier la table "articles" de telle sorte que les articles A01, A02, A03, A04, A05, A06, A09, A10 appartiennent à la catégorie "Fournitures de bureau".
UPDATE articles
SET code_categorie = 'C02'
WHERE code_article IN ('A01', 'A02', 'A03', 'A04', 'A05', 'A06', 'A09', 'A10');

-- 10. Modifier la table "articles" de telle sorte que les articles A07 et A08 appartiennent aux catégories 'Informatique' et 'Électronique' respectivement.
UPDATE articles
SET code_categorie = 'C01' WHERE code_article = 'A07';
UPDATE articles
SET code_categorie = 'C03' WHERE code_article = 'A08';

-- 11. Modifier la table "articles" pour que le fournisseur des articles , A04, A05 et A06 soit 'electrolamp', le fournisseur des articles A09 et A10 soit 'Les stylos reunis', et le fournisseur du reste des articles soit 'Sarl Ali'.
UPDATE articles
SET code_fournisseur = 'F03' WHERE code_article IN ('A04', 'A05', 'A06');
UPDATE articles
SET code_fournisseur = 'F01' WHERE code_article IN ('A09', 'A10');
UPDATE articles
SET code_fournisseur = 'F02' WHERE code_article NOT IN ('A04', 'A05', 'A06', 'A09', 'A10');

-- 12. Modifiez la quantité d'un produit spécifique dans une commande existante dans la table "details_commande".
UPDATE details_commande
SET quantite = 4
WHERE code_commande = 'CMD001C1' AND code_article = 'A01';

-- 13. Supprimez El Amrani Fatima de la table "clients". Assurez-vous que toutes les commandes associées sont également supprimées de la table "commandes".
DELETE FROM clients WHERE code_client = 'CL01';

-- 14. Validez toutes les modifications
COMMIT;

-- Contrôlez la transaction effectuée dans client :

-- 15. Insérez la dernière ligne des données d'exemple dans la table client en exécutant le script que vous avez créé à l'étape 2 (loadclient.sql).
@C:\Users\ousso\Desktop\loadclient.sql

-- 16. Vérifiez l'ajout.
SELECT * FROM clients;

-- 17. Définissez une étiquette intermédiaire (savepoint) dans le traitement de la transaction
SAVEPOINT my_savepoint;

-- 18. Videz entièrement la table client.
DELETE FROM clients;

-- 19. Vérifiez que la table est vide.
SELECT * FROM clients;

-- 20. Annuler la dernière opération DELETE sans annuler l'opération INSERT précédente.
ROLLBACK TO my_savepoint;

-- 21. Vérifiez que la dernière ligne est restée intacte.
SELECT * FROM clients;

-- 22. Validez l’insertion
COMMIT;


