------------- TP2

------------ Exercice1 (Création des Tables)
create table clients(
code_client VARCHAR2(8), 
nom_client VARCHAR2(30), 
prenom_client VARCHAR2(30), 
ville_client VARCHAR2(30), 
email_client VARCHAR2(100), 
type_client VARCHAR2(50),
constraint pk_client primary key(code_client)
);

CREATE TABLE fournisseurs(
code_fournisseur VARCHAR2(8) primary key, 
nom_fournisseur VARCHAR2(100)
);

create table categories(
code_categorie VARCHAR2(8), 
libelle_categorie VARCHAR2(50),
primary key (code_categorie)
);

create table articles(
code_article VARCHAR2(8) primary key, 
libelle_article VARCHAR2(50), 
poids_article NUMERIC(7,2), 
couleur_article VARCHAR2(30), 
prix_vente NUMERIC(7,2), 
prix_achat NUMERIC(7,2), 
stock INTEGER, 
article_fournisseur VARCHAR2(8), 
code_categorie VARCHAR2(8),
constraint fk_categorie_articles FOREIGN key(code_categorie) REFERENCES categories(code_categorie),
constraint fk_fournisseur_articles FOREIGN key(article_fournisseur) REFERENCES fournisseurs(code_fournisseur)
);

create table commandes(
code_commande VARCHAR2(8) primary key, 
code_client VARCHAR2(8),
FOREIGN KEY (code_client) REFERENCES clients(code_client)
);


create table lig_cmd(
code_commande VARCHAR2(8), 
code_article VARCHAR2(8), 
quantite INTEGER,
FOREIGN KEY(code_article) REFERENCES articles(code_article ),
FOREIGN KEY(code_commande) REFERENCES commandes(code_commande),
primary key(code_article,code_commande)
);


CREATE TABLE livreur(
id_livreur VARCHAR2(8) PRIMARY KEY, 
raison_social VARCHAR2(100)
);

create table colis(
code_colis VARCHAR2(8) PRIMARY KEY, 
date_livraison date, 
code_livreur VARCHAR2(8), 
code_commande VARCHAR2(8),
FOREIGN KEY (code_livreur) REFERENCES livreur(id_livreur),
FOREIGN KEY (code_commande) REFERENCES commandes(code_commande)
);

------------- Modification des tables
alter table clients add adresse_client varchar2(100) not null;
alter table commandes add date_commande date;
alter table commandes add nombre_colis integer;
alter table colis add poids number(7,2);
alter table livreur add tarif_km number(7,2);
alter table clients modify ville_client default 'Berkane';
alter table clients modify adresse_client varchar2(255);
rename lig_cmd to details_commande;

----------- Ajout/suppression de contraintes
alter table articles add constraint ck_prix_stock check (prix_vente > 0  AND prix_achat > 0 AND stock > 0);
alter table clients add check (type_client in ('particulier', 'administration', 'grand compte', 'pme'));
alter table articles add constraint uk_libelle_article unique(libelle_article);
alter table clients add unique(email_client);
alter table clients modify ville_client not null;
select constraint_name, column_name from user_cons_columns where table_name = 'COMMANDE'; -- pour chercher le nom de la contrainte
alter table commandes disable constraint SYS_C009113; -- modifier le nom de la contrainte par celui associé à la votre
alter table commandes enable constraint SYS_C009113; -- pour réactiver la contrainte


---------------------------------------------------- TP3 -------------------------------------------------------------------
------------- commencer par supprimer la constrainte d'unicité pour libelle_article et celle de non-nullabilité pour ville_client  

alter table articles drop constraint uk_libelle_article; -- modifier le nom de la contrainte par celui associé à la votre
alter table clients drop constraint SYS_C009126; -- modifier le nom de la contrainte par celui associé à la votre

------------- Insertion des données
insert into articles (code_article, libelle_article, poids_article, couleur_article, prix_vente, prix_achat, stock) 
values ('A01', 'Agrafeuse', 150, 'rouge', 150, 100, 60); -- la valeur -1 pour stock est une violation de contrainte il faut la modifier
---- ou 
insert into articles values ('A02','Calculatrice',150,'Noir',200,200,100,null,null);
insert into articles values ('A03','Cachet dateur',100,'Blanc',300,150,30,null,null);
insert into articles values ('A04', 'Lampe',550,'Rouge',149,105,30,null,null);
insert into articles values ('A05','Lampe',550,'Blanc',149,105,10,null,null);
insert into articles values ('A06', 'Lampe',550,'Bleu',149,105,50,null,null);
insert into articles values ('A07', 'Clavier sans fil',500.0,'Noir',700,400,15,null,null);
insert into articles values ('A08', 'Casque audio',140,'Vert',280,230,15,null,null);
insert into articles values ('A09', 'Crayon',20.0,'rouge',3,1,200,null,null);
insert into articles values ('A10', 'Crayon luxe',20.0,'rouge',6,3,190,null,null);

insert into fournisseurs values ('F01','Les stylos reunis');
insert into fournisseurs values ('F02', 'Sarl Ali');
insert into fournisseurs values ('F03', 'electrolamp');

insert into categories values ('C01', 'Informatique');
insert into categories values ('C02', 'Fournitures de bureau');
insert into categories values ('C03', 'Electronique');


--- pour inserer les clients en mode interactif executer le script loadclient.sql. Utiliser la commande @"chemin"
--- pour le client CL03 la valeur 'entreprise' pour type_client est une violation de contrainte il faut la modifier par une valeur valide, par exemple 'pme'

insert into clients values ('CL01', 'El Amrani', 'Fatima', 'Rabat', 'f.elamrani@gmail.com', 'particulier','15 Avenue Hassan II');
insert into clients values ('CL02', 'Benjelloun', 'Ahmed', 'Casablanca', 'a.benjelloun@gmail.com', 'administration','24 Rue Mohammed V');
insert into clients values ('CL03', 'Oubaha', 'Amina', 'Marrakech', 'am.oubaha@gmail.com', 'pme','10 Rue de la Médina'); -- 
insert into clients values ('CL04', 'El Fassi', 'Karim', 'Casablanca', 'k.elfassi@gmail.com', 'particulier','32 Rue des Artisans');

---------- Création des commandes pour les clients créés jusqu'à maintenant
insert into commandes values('CM01','CL01','12-JAN-2024',1);
insert into commandes values('CM02','CL02',TO_DATE('25/11/2023','DD/MM/YYYY'),2);
insert into commandes values('CM03','CL03',TO_DATE('30/12/2023','DD/MM/YYYY'),2);
insert into commandes values('CM04','CL04',SYSDATE,1);

insert into details_commande values('CM01','A01',1);
insert into details_commande values('CM01','A04',1);
insert into details_commande values('CM01','A05',1);
insert into details_commande values('CM02','A02',2);
insert into details_commande values('CM02','A01',2);
insert into details_commande values('CM03','A03',3);
insert into details_commande values('CM03','A08',3);
insert into details_commande values('CM03','A07',1);
insert into details_commande values('CM04','A04',4);

--- verification des ajouts
SELECT * FROM details_commande
SELECT * FROM commandes;
SELECT * FROM clients;
SELECT * FROM categories;
SELECT * FROM articles;
SELECT * FROM fournisseurs;

--- Validation de la TRANSACTION
COMMIT;

--- Mise à jour et suppression de données
--- Remplacer l’email du client numéro CL03 par a.oubaha@gmail.com
UPDATE clients SET email_client='a.oubaha@gmail.com' WHERE code_client='CL03';

--- Augmenter le prix de vente de l’article ‘A02’ à 235. Le prix actuel de l'article est 200 donc il faut ajouter 35
UPDATE articles SET prix_vente = prix_vente + 35 WHERE code_article='A02';

--- Modifier la table "articles" de telle sorte que les articles A01, A02, A03, A04, A05, A06, A09, A10 appartiennent à la catégorie "Fournitures de bureau".
UPDATE articles SET code_categorie = 'C02' WHERE code_article IN ('A01', 'A02', 'A03', 'A04', 'A05', 'A06', 'A09', 'A10'); -- ou WHERE code_article NOT IN ('A07','A08')

--- Modifier la table "articles" de telle sorte que les articles A07 et A08 appartiennent aux catégories 'Informatique' et 'Électronique' respectivement
UPDATE articles SET code_categorie = 'C01' WHERE code_article = 'A07';

UPDATE articles SET code_categorie = 'C03' WHERE code_article = 'A08';

--- Modifier la table "articles" pour que le fournisseur des articles , A04, A05 et A06 soit 'electrolamp', le fournisseur des articles A09 et A10 soit 'Les stylos reunis', et le fourniseur du reste des articles soit 'Sarl Ali'.
UPDATE articles SET article_fournisseur = 'F03' WHERE code_article  IN ('A04','A05','A06');

UPDATE articles SET article_fournisseur = 'F01' WHERE code_article  IN ('A09','A10');

UPDATE articles SET article_fournisseur = 'F02' WHERE code_article  NOT IN ('A04','A05','A06','A09','A10');

--- Modifiez la quantité d'un produit spécifique dans une commande existante dans la table "details_commande".
UPDATE details_commande SET quantite = 4 WHERE code_commande = 'CM01' AND code_article = 'A05';    

--- Supprimez El Amrani Fatima de la table "clients". Assurez-vous que toutes les commandes associées sont également supprimées de la table "commandes".
DELETE FROM details_commande WHERE code_commande='CM01';
DELETE FROM commandes WHERE code_commande = 'CM01';
DELETE FROM clients WHERE code_client = 'CL01'; 

COMMIT;


--- pour inserer le dernier client en mode interactif executer le script loadclient.sql. Utiliser la commande @"chemin"

--- Vérifiez l'ajout
SELECT * FROM clients;

--- Définissez une étiquette intermédiaire (savepoint) dans le traitement de la transaction
SAVEPOINT insert_done;

--- Videz entièrement la table client
DELETE FROM clients;

--- Vérifiez que la table est vide.
SELECT * FROM clients;

--- Annuler la dernière opération DELETE sans annuler l'opération INSERT précédente.
ROLLBACK TO insert_done;

--- Vérifiez que la dernière ligne est restée intacte.
SELECT * FROM clients;

--- Validez l’insertion
COMMIT;











insert into clients values ('CL05', 'El Hachimi', 'Nour','n.elhachimi@gmail.com', 'administration','5 Boulevard Mohamed VI');

