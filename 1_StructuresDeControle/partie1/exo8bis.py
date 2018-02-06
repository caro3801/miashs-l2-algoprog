"""Affichage de lignes de *"""

from outils import *

nbre = -1
while nbre < 0:
    afficher("Entrez un nombre supérieur ou égal à 0 : ")
    nbre = lire_nombre()

# On connait le nombre d'itérations, donc c'est un for, pas un while...
# Dans cette version, on exploite l'opérateur "*" des chaînes...
for nb_aster in range(nbre, 0, -1):
    afficher_ligne("*" * nb_aster)
