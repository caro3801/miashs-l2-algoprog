"""Affiche le plus petit de 2 nombres donnés par l'utilisateur"""

from outils import *

afficher("Donnez le premier nombre ")
n1 = lire_nombre()
afficher("Donnez le deuxième nombre ")
n2 = lire_nombre()

afficher("Le plus petit des deux est ")
if n1 < n2:
    afficher_ligne(n1)
else:
    afficher_ligne(n2)
