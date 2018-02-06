""" afficher le plus grand de 3 entiers donnés par l'utilisateur """
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
