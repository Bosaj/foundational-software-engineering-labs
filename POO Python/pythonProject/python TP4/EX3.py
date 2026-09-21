class myString:
    def __init__(self, string):
        self.string = string

    def append(self, text):
        self.string += text
    def pop(self, index):
        if 0 <= index < len(self.string):
            self.string =self.string[:index] + self.string[index+1:]
            return self.string
        else:
            return "Index out of range"

# Création d'instance de myString
s1  = myString("Hello")
s2 = myString("bonjour")

# Utilisation des méthode append() and pop()
s1.append(" word !")
s2.pop(2)

# Affichage des résultats
print(s1.string)
print(s2.string)