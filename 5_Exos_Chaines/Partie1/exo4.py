from outils import *

afficher("Entrez une chaîne : ")
chaine = lire_chaine()
afficher("Entrez un caractère : ")
car = lire_chaine()

i = 0
while i < len(chaine) and chaine[i] != car:
    i += 1
if i == len(chaine):
    afficher_ligne(car, "n'est pas dans", chaine)
else:
    afficher_ligne(car, "est à l'indice", i)
