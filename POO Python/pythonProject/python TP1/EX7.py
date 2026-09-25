def calculer_somme_chiffres(nombre):
    somme = 0
    while nombre > 0:
        somme += nombre % 10
        nombre //= 10
    return somme


def determiner_code(entier):
    somme = calculer_somme_chiffres(entier)
    while somme > 9:
        somme = calculer_somme_chiffres(somme)
    return int(str(somme) + str(entier))


while True:
    try:
        n = int(input("Entrez un entier strictement positif et supérieur à 100 : "))
        if n <= 100:
            raise ValueError(
                "le nombre doit être strictement positif et supérieur à 100."
            )
        break
    except ValueError as ve:
        print("Erreur :", ve)

code = determiner_code(n)

print("Le code est : ", code)
