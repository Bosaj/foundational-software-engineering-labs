-- Création de la table etudiants
CREATE TABLE etudiants (
    num_etudiant INT,
    nom VARCHAR(255),
    prenom VARCHAR(255)
);


-- Création de la table matieres
CREATE TABLE matieres (
	code_mat INT,
	libelle_mat VARCHAR(255),
	coeff_mat INT
);

-- Création de la table evaluations
CREATE TABLE evaluations (
    num_etudiant INT,
    code_mat INT,
    "date" DATE,
    note INT
);

-- 1. Ajouter une contrainte de clé primaire sur les colonnes 'num_etudiant' et 'code_mat' des tables etudiants et matieres
ALTER TABLE etudiants ADD CONSTRAINT pk_etudiants PRIMARY KEY (num_etudiant);
ALTER TABLE matieres ADD CONSTRAINT pk_matieres PRIMARY KEY (code_mat);

-- 2. Ajouter une contrainte de clé étrangère sur la colonne 'num_etudiant' de la table evaluations, faisant référence à la colonne 'num_etudiant' de la table etudiants.
ALTER TABLE evaluations ADD CONSTRAINT fk_evaluations_etudiants FOREIGN KEY (num_etudiant) REFERENCES etudiants(num_etudiant);

-- 3. Ajouter une contrainte de clé étrangère sur la colonne 'code_mat' de la table evaluations, faisant référence à la colonne code_mat de la table matieres.
ALTER TABLE evaluations ADD CONSTRAINT fk_evaluations_matieres FOREIGN KEY (code_mat) REFERENCES matieres(code_mat);

-- 4. Ajouter une contrainte de clé primaire composée de 'num_etudiant' et 'code_mat' dans la table evaluations
ALTER TABLE evaluations ADD CONSTRAINT pk_evaluations PRIMARY KEY (num_etudiant, code_mat);

-- 5. Ajouter une contrainte pour s’assurer que les libellés des matières sont uniques
ALTER TABLE matieres ADD CONSTRAINT unique_libelle_mat UNIQUE (libelle_mat);

-- 6. Ajouter une contrainte pour que l’attribut 'coeff_mat' soit strictement positif
ALTER TABLE matieres ADD CONSTRAINT check_coeff_mat_positive CHECK (coeff_mat > 0);

--Pour supprimer les tables
DROP TABLE evaluations;

DROP TABLE matieres;

DROP TABLE etudiants;