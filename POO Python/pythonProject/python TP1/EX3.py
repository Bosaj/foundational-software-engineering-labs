# try:
#     n = int (input("Saisir un nombre n : "))
#     if n == 0:
#         print(1)
#     else:
#         fact = 1
#         for k in range(2, n + 1):
#             fact = fact * k
#         print(fact)
# except ValueError:
#     print("Oups, vous avez saisi autre chose que nombre")

def factorielle(n):
    if n == 0:
        return 1
    else:
        return n * factorielle(n - 1)


while True:
    nombre_entier = int(input("Entrez un nombre entier positif : "))
    while True:
        try:
            if nombre_entier < 0:
                raise ValueError("Le nombre doit être positif.")
            break
        except ValueError as ve:
            print(ve)

    resultat = factorielle(nombre_entier)
    print(f"{nombre_entier}! = {resultat}")
