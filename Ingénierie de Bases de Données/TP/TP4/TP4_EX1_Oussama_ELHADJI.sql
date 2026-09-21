-- 1. Afficher tous les noms de fournisseurs
SELECT nom_fournisseur FROM fournisseurs;

-- 2. Rechercher la liste des différentes villes où habitent les clients
SELECT DISTINCT ville_client FROM clients;

-- 3. Retrouver tous les clients habitant à casablanca
SELECT * FROM clients WHERE ville_client = 'Casablanca';

-- 4. Sélectionner tous les articles dont le poids est supérieur à 500
SELECT * FROM articles WHERE poids_article > 500;

-- 5. Sélectionner tous les articles pour lesquels le prix de vente est supérieur ou égal au double du prix d’achat.
SELECT * FROM articles WHERE prix_vente >= 2 * prix_achat;

-- 6. Sélectionner tous les articles rouges de poids supérieurs à 100.
SELECT * FROM articles WHERE couleur_article = 'rouge' AND poids_article > 100;

-- 7. Sélectionner tous les articles rouges et ceux de poids supérieurs à 500
SELECT * FROM articles WHERE couleur_article = 'rouge' OR poids_article > 500;

-- 8. L’inverse de la question 7
SELECT * FROM articles WHERE NOT (couleur_article = 'rouge' OR poids_article > 500);

-- 9. Sélectionner tous les articles dont, soit la couleur est rouge et le poids est supérieur à 100, soit la couleur est verte.
SELECT * FROM articles WHERE (couleur_article = 'rouge' AND poids_article > 100) OR couleur_article = 'verte';

-- 10. Afficher la liste des articles dont le prix de vente est compris entre 100 et 150.
SELECT * FROM articles WHERE prix_vente BETWEEN 100 AND 150;

-- 11. Afficher la liste des articles de couleur soit rouge, soit verte
SELECT * FROM articles WHERE couleur_article IN ('rouge', 'verte');

-- 12. Afficher les clients dont le prénom commence par 'A'
SELECT * FROM clients WHERE prenom_client LIKE 'A%';

-- 13. Afficher les clients dont le nom commence par 'O' et le 4eme caractère est 'a'
SELECT * FROM clients WHERE nom_client LIKE 'O_a%';

-- 14. Rechercher tous les articles pour lesquels on a négligé la couleur.
SELECT * FROM articles WHERE couleur_article IS NULL;

-- 15. Trier les articles selon l’ordre croissant de leurs poids.
SELECT * FROM articles ORDER BY poids_article ASC;

-- 16. Trier les articles de poids inférieur ou égal à 100 selon l’ordre croissant de leur poids et par ordre décroissant de leurs prix d’achat.
SELECT * FROM articles WHERE poids_article <= 100 ORDER BY poids_article ASC, prix_achat DESC;

-- 17. Afficher la marge bénéficiaire sur les articles dont le prix d’achat est supérieur à 100, par ordre de celle-ci.
SELECT *, prix_vente - prix_achat AS marge FROM articles WHERE prix_achat > 100 ORDER BY marge;

-- 18. Pour tous les clients habitant casa, afficher le nom complet
SELECT CONCAT(nom_client, ' ', prenom_client) AS nom_complet FROM clients WHERE ville_client = 'Casablanca';

-- 19. Calculer le poids moyen des articles
SELECT AVG(poids_article) AS poids_moyen FROM articles;

-- 20. Calculer le prix de l’article le plus cher du stock.
SELECT MAX(prix_vente) AS prix_max FROM articles;

-- 21. Compter le nombre de couleurs différentes des articles existants.
SELECT COUNT(DISTINCT couleur_article) AS nombre_couleurs FROM articles;

-- 22. Calculer le prix de vente moyen de chaque couleur d’articles. Trier le résultat par couleur.
SELECT couleur_article, AVG(prix_vente) AS prix_vente_moyen FROM articles GROUP BY couleur_article ORDER BY couleur_article;

-- 23. Calculer le prix de vente moyen des articles de chaque couleur en excluant les articles pour lesquels le prix d’achat est inférieur à 100
SELECT couleur_article, AVG(prix_vente) AS prix_vente_moyen FROM articles WHERE prix_achat > 100 GROUP BY couleur_article;

-- 24. Rechercher la couleur des articles dont le prix de vente moyen des articles de la couleur est supérieur à 100.
SELECT couleur_article FROM articles GROUP BY couleur_article HAVING AVG(prix_vente) > 100;

-- Sous requêtes et Jointures :
-- 25. Afficher les noms de tous les articles ayant la même catégorie que l’article ‘Agrafeuse’ à l'exclusion de ce dernier
SELECT a2.libelle_article
FROM articles a1
JOIN articles a2 ON a1.code_categorie = a2.code_categorie
WHERE a1.libelle_article = 'Agrafeuse' AND a2.libelle_article != 'Agrafeuse';

-- 26. Afficher tous les articles dont le prix de vente est supérieur de la moyenne de tous les prix. Triez les résultats par ordre décroissant des prix
SELECT *
FROM articles
WHERE prix_vente > (SELECT AVG(prix_vente) FROM articles)
ORDER BY prix_vente DESC;

-- 27. Afficher le nom et la ville de tous les clients qui habitent dans la même ville que tout client dont le prénom contient un A.
SELECT c2.nom_client, c2.ville_client
FROM clients c1
JOIN clients c2 ON c1.ville_client = c2.ville_client
WHERE c1.prenom_client LIKE '%A%';

-- 28. Obtenir la liste des articles disponibles dans la catégorie Informatique
SELECT *
FROM articles a
JOIN categories c ON a.code_categorie = c.code_categorie
WHERE c.libelle_categorie = 'Informatique';

-- 29. Afficher tous les articles dont la marge bénéficiaire est supérieure à la moyenne des marges bénéficiaires de tous les articles
SELECT *
FROM articles
WHERE prix_vente - prix_achat > (SELECT AVG(prix_vente - prix_achat) FROM articles);

-- 30. Afficher tous les articles ayant le même prix d’achat ou la même quantité de stock qu’un article Lampe
SELECT *
FROM articles
WHERE prix_achat = (SELECT prix_achat FROM articles WHERE libelle_article = 'Lampe')
OR stock = (SELECT stock FROM articles WHERE libelle_article = 'Lampe');

-- 31. Trouver tous les clients qui ont passé des commandes avec un nombre de colis supérieur à la moyenne
SELECT c.*
FROM clients c
JOIN commandes cmd ON c.code_client = cmd.code_client
JOIN colis cl ON cmd.code_commande = cl.code_commande
GROUP BY c.code_client
HAVING COUNT(cl.code_colis) > (SELECT AVG(cnt) FROM (SELECT COUNT(cl.code_colis) AS cnt FROM colis cl GROUP BY cl.code_commande));

-- 32. Trouver les clients qui ont commandé une calculatrice
SELECT c.*
FROM clients c
JOIN commandes cmd ON c.code_client = cmd.code_client
JOIN lig_cmd lc ON cmd.code_commande = lc.code_commande
JOIN articles a ON lc.code_article = a.code_article
WHERE a.libelle_article = 'Calculatrice';

-- 33. Afficher les commandes avec leurs détails pour une date spécifique.
SELECT *
FROM commandes cmd
JOIN lig_cmd lc ON cmd.code_commande = lc.code_commande
JOIN articles a ON lc.code_article = a.code_article
JOIN colis cl ON cmd.code_commande = cl.code_commande
WHERE cl.date_livraison = TO_DATE('2023-01-01', 'YYYY-MM-DD');

-- 34. Calculer le montant total de toutes les commandes passées
SELECT SUM(a.prix_vente * lc.quantite) AS montant_total
FROM articles a
JOIN lig_cmd lc ON a.code_article = lc.code_article;

-- 35. Afficher les fournisseurs qui fournissent des articles de la catégorie 'Électronique'
SELECT DISTINCT f.*
FROM fournisseurs f
JOIN articles a ON f.code_fournisseur = a.code_fournisseur
JOIN categories c ON a.code_categorie = c.code_categorie
WHERE c.libelle_categorie = 'Électronique';

-- 36. Trouver les articles dont le prix de vente est supérieur à la moyenne des prix de vente des articles de la même catégorie
SELECT a.*
FROM articles a
JOIN (SELECT code_categorie, AVG(prix_vente) AS avg_prix_vente FROM articles GROUP BY code_categorie) avg_prices
ON a.code_categorie = avg_prices.code_categorie
WHERE a.prix_vente > avg_prices.avg_prix_vente;
