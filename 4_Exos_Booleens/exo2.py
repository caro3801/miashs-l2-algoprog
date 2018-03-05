""" afficher le plus grand de 3 entiers donnés par l'utilisateur """

"""
DEBUT
afficher("Entrez un nombre : ")
lire(nb1)
afficher("Entrez un nombre : ")
lire(nb2)
afficher("Entrez un nombre : ")
lire(nb3)

afficher("Le plus grand des trois est ")

SI nb1 >= nb2 ALORS
    SI nb1 >= nb3 ALORS
        afficher(nb1)
    SINON
        afficher(nb3)
    FINSI
SINON
    SI nb2 >= nb3 ALORs
        afficher(nb2)
    SINON
        afficher(nb3)
    FSI
FSI

FIN
"""
from outils import *

afficher("Entrez un nombre : ")
nb1 = lire_nombre()
afficher("Entrez un nombre : ")
nb2 = lire_nombre()
afficher("Entrez un nombre : ")
nb3 = lire_nombre()

print("Le plus grand des trois est ", end="")
if nb1 >= nb2:
    if nb1 >= nb3:
        print(nb1)
    else:
        print(nb3)
else:
    if nb2 >= nb3:
        print(nb2)
    else:
        print(nb3)
