# Correction du prof
def auteur(liste):
    result = {}
    for livre in liste:
        if livre["auteur"] not in result:
            result[livre["auteur"]] = []
        result[livre["auteur"]].append(livre["titre"])
    return result


# Méthode 1 : Utilisation d'une boucle for
def livres_par_auteur_boucle_for(livres):
    livres_par_auteur = {}
    for livre in livres:
        auteur = livre["auteur"]
        titre = livre["titre"]
        if auteur not in livres_par_auteur:
            livres_par_auteur[auteur] = [titre]
        else:
            livres_par_auteur[auteur].append(titre)
    return livres_par_auteur


# Méthode 2 : Utilisation d'une boucle for avec setdefault()
def livres_par_auteur_setdefault(livres):
    livres_par_auteur = {}
    for livre in livres:
        auteur = livre["auteur"]
        titre = livre["titre"]
        livres_par_auteur.setdefault(auteur, []).append(titre)
    return livres_par_auteur


# Méthode 3 : Utilisation d'une compréhension de dictionnaire
def livres_par_auteur_comprehension_dict(livres):
    return {
        auteur: [livre["titre"] for livre in livres if livre["auteur"] == auteur]
        for auteur in {livre["auteur"] for livre in livres}
    }


# Dictionnaire des livres
livres = [
    {"titre": "Dune", "auteur": "Frank Herbert"},
    {"titre": "1984", "auteur": "George Orwell"},
    {"titre": "Le Meilleur des mondes", "auteur": "Aldous Huxley"},
    {"titre": "Fondation", "auteur": "Isaac Asimov"},
    {"titre": "La Ferme des animaux", "auteur": "George Orwell"},
]

# Test de chaque méthode
print("Méthode 1 (boucle for) :", livres_par_auteur_boucle_for(livres))
print(
    "Méthode 2 (boucle for avec setdefault()) :", livres_par_auteur_setdefault(livres)
)
print(
    "Méthode 3 (compréhension de dictionnaire) :",
    livres_par_auteur_comprehension_dict(livres),
)
