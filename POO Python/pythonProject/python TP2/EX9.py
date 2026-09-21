# Exercice 9
def estdistinct(nb):
    chiffres = set(str(nb))
    if len(chiffres) == len(str(nb)):
        print("Cet entier est distinct.")
    else:
        print("Cet entier est non distinct.")

# Tests
print(estdistinct(1273))  # Devrait afficher "Cet entier est distinct."
print(estdistinct(1565))  # Devrait afficher "Cet entier est non distinct."














































