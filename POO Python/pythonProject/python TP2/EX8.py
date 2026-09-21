# Exercice 8
def extraire_domaine(email):
    partie_domaine = email.split('@')[1]
    domaine = partie_domaine.split()[0]
    return domaine
