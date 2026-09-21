def calculer_ttc(prix_hors_taxe, categories):
    if categories == 'A':
        tva = 0.07
    elif categories == 'B':
        tva = 0.20
    elif categories == 'C':
        tva = 0.25
    else:
        raise ValueError("Catégorie invalide.")
    prix_toutes_taxes_comprises = prix_hors_taxe * (1 + tva)
    return prix_toutes_taxes_comprises


while True:
    prix_ht = float(input("Entrez le prix hors taxe du produit : "))
    categorie = input("Entrez la catégorie du produit (A, B ou C) : ").upper()
    while True:
        try:
            if categorie not in ['A', 'B', 'C']:
                raise ValueError("Catégorie invalide.")
            break  # Sortir de la boucle si l'entrée est valide
        except ValueError as ve:
            print("Erreur :", ve)

    prix_ttc = calculer_ttc(prix_ht, categorie)
    print(f"Le prix toutes taxes comprises (TTC) du produit est : {prix_ttc:.3f} euros")
