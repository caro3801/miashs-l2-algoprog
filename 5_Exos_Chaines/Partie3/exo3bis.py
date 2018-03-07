from outils import *

afficher("Entrez une chaîne : ")
chaine = lire_chaine()
afficher("Entrez un caractère : ")
car = lire_chaine()

cpt = chaine.count(car)

afficher_ligne(car, "apparaît", cpt, "fois dans", chaine)
