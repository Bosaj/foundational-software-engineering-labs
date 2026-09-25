class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age

    def __str__(self):
        return f"Nom: {self.nom}, Âge: {self.age}"


class Employe(Personne):
    def __init__(self, nom, age, salaire):
        super().__init__(nom, age)
        self._salaire = salaire

    def show_salary(self):
        print(f"Le salaire de {self.nom} et {self._salaire}")


class Manager(Employe):
    pass


# Création l'objets avec les différentes classes
personne1 = Personne("Alice", 30)
employe1 = Employe("Bob", 25, 50000)
manager1 = Manager("Charlie", 35, 80000)

# Affichage des informations des objets
print(personne1)
employe1.show_salary()
manager1.show_salary()
