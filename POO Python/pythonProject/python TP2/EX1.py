import math

def cube(x):
    return x ** 3

def volumeSphere(rayon):
    volume = (4 * math.pi * cube(rayon)) / 3
    return volume

if __name__ == "__main__":
    try:
        rayon = float(input("Entrez le rayon de la sphère : "))

        volume = volumeSphere(rayon)

        print(f"Le volume de la sphère de rayon {rayon} est : {volume}")
    except ValueError:
        print("Erreur : Veuillez entrer un nombre valide.")
