from outils import *

afficher("Entrez une chaîne : ")
chaine = lire_chaine()
afficher("Entrez un caractère : ")
car = lire_chaine()

chaine2=chaine.upper()
car2=car.upper()

cpt=chaine2.count(car2)

afficher_ligne(car, "apparaît", cpt, "fois dans", chaine)
