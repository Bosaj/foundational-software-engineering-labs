# Liste avec doublons
list_doublons = [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 7, 8, 9, 10]

# Méthode 1 : Utilisation de l'opérateur 'in'
liste_sans_doublons_in = []
[liste_sans_doublons_in.append(element) for element in list_doublons if element not in liste_sans_doublons_in]

# Méthode 2 : Utilisation de la méthode count()
liste_sans_doublons_count = []
[liste_sans_doublons_count.append(element) for element in list_doublons if list_doublons.count(element) == 1]

# Méthode 3 : Utilisation de la conversion en ensemble (set)
liste_sans_doublons_set = list(set(list_doublons))

# Méthode 4 : Utilisation de la fonction OrderedDict de la bibliothèque collections
from collections import OrderedDict
liste_sans_doublons_ordered = list(OrderedDict.fromkeys(list_doublons))

# Méthode 5 : Utilisation de la méthode remove() avec une boucle
liste_sans_doublons_remove = list(list_doublons)
for element in list_doublons:
    while liste_sans_doublons_remove.count(element) > 1:
        liste_sans_doublons_remove.remove(element)

# Méthode 6 : Utilisation de la méthode comprehension de liste avec filter
liste_sans_doublons_filter = list(filter(lambda x: list_doublons.count(x) == 1, list_doublons))

# Affichage des listes sans doublons obtenues avec chaque méthode
print("Liste sans doublons (utilisant l'opérateur 'in') :", liste_sans_doublons_in)
print("Liste sans doublons (utilisant la méthode count()) :", liste_sans_doublons_count)
print("Liste sans doublons (utilisant la conversion en ensemble) :", liste_sans_doublons_set)
print("Liste sans doublons (utilisant la fonction OrderedDict) :", liste_sans_doublons_ordered)
print("Liste sans doublons (utilisant la méthode remove() avec une boucle) :", liste_sans_doublons_remove)
print("Liste sans doublons (utilisant la méthode comprehension de liste avec filter) :", liste_sans_doublons_filter)



#---Version avec les méthodes de liste :
def enlever_doublons_methodes(liste):
    return list(set(liste))

# Liste avec doublons
list_doublons = [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 7, 8, 9, 10]

# Enlever les doublons en utilisant les méthodes de liste
resultat_methodes = enlever_doublons_methodes(list_doublons)

print("Résultat (utilisant les méthodes de liste) :", resultat_methodes)
