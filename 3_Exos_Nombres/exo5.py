"""Déterminer si un nombre saisi est un multiple de 5"""

from outils import *

afficher("Entrez un nombre : ")
nbre = lire_nombre()

if nbre % 5 == 0:
    afficher_ligne(nbre, "est un multiple de 5")
else:
    afficher_ligne(nbre, "n'est pas un multiple de 5")
