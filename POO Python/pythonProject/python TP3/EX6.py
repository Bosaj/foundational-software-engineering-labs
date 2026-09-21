# Méthode 1 : Utilisation de la méthode index()
def trouver_position_index(element, mon_tuple):
    try:
        position = mon_tuple.index(element)
        return position
    except ValueError:
        return -1

# Méthode 2 : Utilisation d'une boucle for
def trouver_position_boucle(element, mon_tuple):
    for i in range(len(mon_tuple)):
        if mon_tuple[i] == element:
            return i
    return -1

# Méthode 3 : Utilisation de la fonction enumerate() avec une boucle for
def trouver_position_enumerate(element, mon_tuple):
    for i, value in enumerate(mon_tuple):
        if value == element:
            return i
    return -1

# Méthode 4 : Utilisation de la méthode index() avec gestion des exceptions
def trouver_position_index_exception(element, mon_tuple):
    try:
        return mon_tuple.index(element)
    except ValueError:
        return -1

# Tuple de test
mon_tuple = (1, 2, 3, 4, 5)

# Élément à rechercher
element_recherche = 3

# Test de chaque méthode
print("Méthode 1 (index()) :", trouver_position_index(element_recherche, mon_tuple))
print("Méthode 2 (boucle for) :", trouver_position_boucle(element_recherche, mon_tuple))
print("Méthode 3 (enumerate()) :", trouver_position_enumerate(element_recherche, mon_tuple))
print("Méthode 4 (index() avec gestion des exceptions) :", trouver_position_index_exception(element_recherche, mon_tuple))
