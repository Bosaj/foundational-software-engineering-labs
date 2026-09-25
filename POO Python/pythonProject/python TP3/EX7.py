# Corrigé :
def fun(t):
    x = max(t)
    y = min(t)
    return y, x


T = (1, 5, 3, 8, 2, 7)
print("Corrié du etudiant :", fun(T))


# Méthode 1 : Utilisation des fonctions min() et max()
def trouver_min_max_min_max(mon_tuple):
    return (min(mon_tuple), max(mon_tuple))


# Méthode 2 : Utilisation de l'opérateur de comparaison et d'une boucle for
def trouver_min_max_comparaison(mon_tuple):
    min_val = float("inf")  # initialiser min_val à une valeur infinie
    max_val = float("-inf")  # initialiser max_val à une valeur moins l'infini
    for num in mon_tuple:
        min_val = min(min_val, num)
        max_val = max(max_val, num)
    return (min_val, max_val)


# Méthode 3 : Utilisation de la fonction sorted() avec un slicing
def trouver_min_max_sorted(mon_tuple):
    sorted_tuple = sorted(mon_tuple)
    return (sorted_tuple[0], sorted_tuple[-1])


# Tuple de test
mon_tuple = (1, 5, 3, 8, 2, 7)

# Test de chaque méthode
print("Méthode 1 (min() et max()) :", trouver_min_max_min_max(mon_tuple))
print(
    "Méthode 2 (opérateur de comparaison et boucle for) :",
    trouver_min_max_comparaison(mon_tuple),
)
print("Méthode 3 (sorted() avec slicing) :", trouver_min_max_sorted(mon_tuple))
