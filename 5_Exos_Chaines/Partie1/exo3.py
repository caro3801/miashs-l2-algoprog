from outils import *

afficher("Entrez une chaîne : ")
chaine = lire_chaine()
afficher("Entrez un caractère : ")
car = lire_chaine()

cpt = 0
for c in chaine:
    # if c == car:
    #    cpt = cp + 1
    cpt = cpt + 1 if c == car else cpt

afficher_ligne(car, "apparaît", cpt, "fois dans", chaine)
