class Compte:
    def __init__(self, nom, numero, balance):
        self.nom = nom
        self.numero = numero
        self.balance = balance

    def deposer(self, montant):
        self.balance += montant

    def retirer(self, montant):
        self.balance -= montant


# Création d'une instance de la classe Compte pour Asmaa
asmaa_compte = Compte("Asmaa", 12345, 20000)

# Dépôt initial de 3000DH
asmaa_compte.deposer(3000)

# Retrait de 800DH
asmaa_compte.retirer(800)

# Affichage du solde final du compte d'Asmaa
print(f"Le solde du compte d'Asmaa est de {asmaa_compte.balance}DH")
