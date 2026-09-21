def calculer_somme(nombre):
    somme = 0
    for i in range(1, nombre + 1):
        somme += i
    return somme


while True:
    try:
        n = int(input("Entrez un nombre entier positif : "))
        if n <= 0:
            raise ValueError("Le nombre doit être positif.")
        break
    except ValueError as ve:
        print(ve)
resultat = calculer_somme(n)
print(f"La somme des nombre de 1 à {n} est : {resultat}")
