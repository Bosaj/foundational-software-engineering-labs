# Exercice 4
def compter_voyelles(chaine):
    voyelles = "aeiouAEIOU"
    nb_voyelles = 0
    for char in chaine:
        if char in voyelles:
            nb_voyelles += 1
    return nb_voyelles
