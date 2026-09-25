# Corrigé du Etudiant :
def commul(liste):
    commul = []
    sum = 0
    for i in liste:
        sum += i
        commul.append(sum)
    return commul


liste = [1, 2, 3, 4]
print(commul(liste))


# Méthode 1 : Utilisation d'une boucle for
def cumul_valeurs_boucle_for(liste):
    cumul = []
    total = 0
    for valeur in liste:
        total += valeur
        cumul.append(total)
    return cumul


# Méthode 2 : Utilisation d'une compréhension de liste
def cumul_valeurs_comprehension_liste(liste):
    cumul = [sum(liste[: i + 1]) for i in range(len(liste))]
    return cumul


# Méthode 3 : Utilisation de la fonction accumulate() de la bibliothèque itertools
from itertools import accumulate


def cumul_valeurs_itertools(liste):
    return list(accumulate(liste))


# Méthode 4 : Utilisation de la fonction reduce() de la bibliothèque functools
from functools import reduce


def cumul_valeurs_fonction_reduce(liste):
    cumul = []
    reduce(
        lambda total, valeur: cumul.append(total + valeur) or total + valeur, liste, 0
    )
    return cumul


# Tests avec les exemples d'utilisation
liste1 = [1, 4, 7]
liste2 = [1, 2, 3, 4, 5, 6]
liste3 = []

# Test de chaque méthode
print("Méthode 1 (boucle for) :", cumul_valeurs_boucle_for(liste1))
print("Méthode 2 (compréhension de liste) :", cumul_valeurs_comprehension_liste(liste2))
print("Méthode 3 (itertools) :", cumul_valeurs_itertools(liste3))
print("Méthode 4 (functools.reduce) :", cumul_valeurs_fonction_reduce(liste3))
