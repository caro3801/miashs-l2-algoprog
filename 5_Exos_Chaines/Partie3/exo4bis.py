from outils import *

afficher("Entrez une chaîne : ")
chaine = lire_chaine()
afficher("Entrez un caractère : ")
car = lire_chaine()

i = chaine.find(car)

if i == -1:
    afficher_ligne(car, "n'est pas dans", chaine)
else:
    afficher_ligne(car, "est à l'indice", i)
