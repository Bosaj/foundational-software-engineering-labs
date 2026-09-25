# Méthode 1 : Utilisation d'une boucle for
def moyenne_eleves_boucle_for(notes_eleves):
    moyennes = {}
    for eleve, notes in notes_eleves.items():
        moyenne = sum(notes) / len(notes)
        moyennes[eleve] = moyenne
    return moyennes


# Méthode 2 : Utilisation d'une compréhension de dictionnaire
def moyenne_eleves_comprehension_dict(notes_eleves):
    return {eleve: sum(notes) / len(notes) for eleve, notes in notes_eleves.items()}


# Méthode 3 : Utilisation de la fonction map() avec une fonction lambda
def moyenne_eleves_map_lambda(notes_eleves):
    return {x[0]: sum(x[1]) / len(x[1]) for x in notes_eleves.items()}


# Méthode 4 : Utilisation de la fonction zip() avec une fonction lambda
def moyenne_eleves_zip_lambda(notes_eleves):
    return dict(
        zip(notes_eleves.keys(), (sum(x) / len(x) for x in notes_eleves.values()))
    )


# Dictionnaire des notes des élèves
notes_eleves = {"Alice": [15, 16, 14], "Bob": [18, 17, 19], "Charlie": [12, 14, 13]}

# Test de chaque méthode
print("Méthode 1 (boucle for) :", moyenne_eleves_boucle_for(notes_eleves))
print(
    "Méthode 2 (compréhension de dictionnaire) :",
    moyenne_eleves_comprehension_dict(notes_eleves),
)
print("Méthode 3 (map() avec lambda) :", moyenne_eleves_map_lambda(notes_eleves))
print("Méthode 4 (zip() avec lambda) :", moyenne_eleves_zip_lambda(notes_eleves))
