--Création de Tables :

--1.Créer la base de données correspondante

-- Création de la table Clients
CREATE TABLE clients(
	code_client VARCHAR(8) PRIMARY KEY,
	nom_client VARCHAR(255),
	prenom_client VARCHAR(255),   
	ville_client  VARCHAR(255),
	email_client VARCHAR(255),
	type_client VARCHAR(255)
);

-- Création de la table fournisseurs
CREATE TABLE fournisseurs(
	code_fournisseur VARCHAR(8) PRIMARY KEY,
	nom_fournisseur  VARCHAR(255)
);

-- Création de la table categories
CREATE TABLE categories(
	code_categorie VARCHAR(8) PRIMARY KEY,
    libelle_categorie VARCHAR(255)
);

-- Création de la table articles
CREATE TABLE articles(
	code_article VARCHAR(8) PRIMARY KEY,
	libelle_article VARCHAR(255),
	poids_article NUMBER(7,2),
	couleur_article VARCHAR(255),
	prix_vente NUMBER(7,2),
	prix_achat NUMBER(7,2),
	stock INT,
	code_fournisseur VARCHAR(255),
	code_categorie VARCHAR(255),
		CONSTRAINT articles_code_fournisseur_fk FOREIGN KEY(code_fournisseur) 
				REFERENCES fournisseurs (code_fournisseur),
	CONSTRAINT articles_code_categorie_fk FOREIGN KEY(code_categorie) 
				REFERENCES categories (code_categorie)
);

-- Création de la table commandes
CREATE TABLE commandes(
	code_commande VARCHAR(8) PRIMARY KEY,
	code_client VARCHAR(8),
		CONSTRAINT commandes_code_client_fk FOREIGN KEY(code_client)
                                             REFERENCES clients (code_client)
);

-- Création de la table lig_cmd (lig_cmd étant une abréviation de ligne_commande)
CREATE TABLE lig_cmd(
	code_commande VARCHAR(8) REFERENCES commandes(code_commande),
	code_article VARCHAR(8) REFERENCES articles(code_article),
	quantite INT,
		CONSTRAINT lig_cmd_code_pk  PRIMARY KEY(code_commande,code_article)
);

-- Création de la table livreur
CREATE TABLE livreur(
	id_livreur VARCHAR(8) PRIMARY KEY,
	raison_social VARCHAR(255)
);

-- Création de la table colis
CREATE TABLE colis(
	code_colis VARCHAR(8) PRIMARY KEY,
	date_livraison DATE,
	id_livreur VARCHAR(8),
	code_commande VARCHAR(8),
		CONSTRAINT colis_id_livreur_fk FOREIGN KEY(id_livreur)
				REFERENCES livreur (id_livreur),
		CONSTRAINT colis_code_commande_fk FOREIGN KEY(code_commande)
				REFERENCES commandes (code_commande)
);


--2.Vérifier l’existence des tables créées :
SELECT table_name FROM user_tables;


--Modification des tables :

--1. Ajouter une colonne 'adresse_client' à la table clients. La colonne ne doit pas être nulle et sa taille doit être fixé à 100 caractères
ALTER TABLE clients
ADD	(adresse_client VARCHAR(100) NOT NULL);

--2. Ajouter une colonne 'date_commande' à la table commandes pour stocker la date d’une commande
ALTER TABLE commandes
ADD	(date_commande DATE);

--3. Ajouter une colonne 'nombre_colis' à la table commandes
ALTER TABLE commandes
ADD	(nombre_colis INT);

--4. Ajouter une colonne 'poids' à la table colis
ALTER TABLE colis
ADD	(poids  NUMBER(7,2));

--5. Ajouter une colonne 'tarif_km' à la table livreur
ALTER TABLE livreur
ADD	(tarif_km  NUMBER(7,2));

--6. Modifier la colonne 'ville_client' dans la table clients pour lui attribuer une valeur par défaut de 'Berkane'
ALTER TABLE clients
MODIFY	(ville_client  DEFAULT 'Berkane');

--7. Modifier la colonne 'adresse_client' de la table clients pour augmenter sa taille à 255
ALTER TABLE clients
MODIFY	(adresse_client  VARCHAR(255));

--8.Changer le nom de la table lig_cmd en details_commande
ALTER TABLE lig_cmd
RENAME TO details_commande;

--Ajout/suppression de contraintes :

--Ajouter une contrainte pour que les attributs prix_vente, prix_achat et stock,de la table articles aient des valeurs strictement positive
ALTER TABLE articles
ADD CONSTRAINT ck_prix_stock_positive
CHECK (prix_vente > 0 AND prix_achat > 0 AND stock > 0);

--2. Ajouter une contrainte à la table clients pour garantir que la colonne 'type_client' ne puisse contenir que l'une des valeurs suivantes: 'particulier', 'administration', 'grand compte' ou 'pme'
ALTER TABLE clients
ADD CONSTRAINT check_type_client
CHECK (type_client IN ('particulier', 'administration', 'grand compte', 'pme'));

--3. Ajouter une contrainte pour s’assurer que les libellées des articles sont uniques
ALTER TABLE articles
ADD CONSTRAINT unique_libelle_article UNIQUE(libelle_article);


--4. Ajoutez une contrainte pour vous assurer que la colonne 'email_client' de la table clients est unique
ALTER TABLE clients
ADD CONSTRAINT unique_email_client UNIQUE(email_client);


--5.Ajouter une contrainte pour garantir que la colonne 'ville_client' ne soit pas nulle
ALTER TABLE clients
MODIFY (ville_client NOT NULL);
--OR
ALTER TABLE clients
ADD CONSTRAINT check_ville_client_notnull
CHECK(ville_client IS NOT NULL);


--6.Désactiver la contrainte de la clé étrangère 'code_client' de la table commandes
ALTER TABLE commandes
DISABLE CONSTRAINT commandes_code_client_fk;






