#Exercice 3
#--Définir la liste: liste =[17, 38, 10, 25, 72, -1, 16, 82, 0.5], puis effectuez les actions suivantes :

l = [17,38,10,25,72,-1,16]
l_cop = l.copy()
#l_cop = l[:]
#l-cop = sorted(l)

#--Triez et affichez la liste
l_cop.sort()

#--Ajoutez l’élément 12 à la liste et affichez la liste
l_cop.append(12) # l_cop = l_cop + [12]

#--Renversez et affichez la liste
l_cop.reverse() #l_cop = l_cop[::-1]
print(l_cop)

#--Affichez l’indice de l’élément 17
print(l_cop.index(17))

#--Enlevez l’élément 38 et affichez la liste
l_cop.remove(38)
print(l_cop)

#--Affichez la sous-liste du 2e au 3e élément
print(l_cop[1:3])

#--Affichez la sous-liste du début au 2e élément
print(l_cop[:2])

#--Affichez la sous-liste du 3e élément à la fin de la liste
print(l_cop[2:])

#--Affichez la sous-liste complète de la liste
print(l_cop[:])

#--Affichez le premier et le dernier élément
print(l_cop[::len(l_cop) - 1])
