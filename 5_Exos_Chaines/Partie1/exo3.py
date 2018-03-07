"""compter le nombre de fois qu'une lettre apparaît dans
une chaine de caractères ; la lettre et la chaine de
caractères sont données par l'utilisateur."""

"""
DEBUT
afficher("Entrez une chaine de caractere : ")
lire(phrase)
afficher("Quel caractere compter?  ")
lire(car)
cpt = 0
POUR c in chaine:
    SI c == car:
        cpt = cp + 1
    FSI
FPOUR
afficher_ligne(car, "apparaît", cpt, "fois dans", chaine)

FIN
"""

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
