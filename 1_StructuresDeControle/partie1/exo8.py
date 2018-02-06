"""Affichage de lignes de *"""

from outils import *

nbre = -1
while nbre < 0:
    afficher("Entrez un nombre supérieur ou égal à 0 : ")
    nbre = lire_nombre()
    
# On connait le nombre d'itérations, donc c'est un for, pas un while...
for nb_aster in range(nbre, 0, -1):
    for _ in range(nb_aster):
        afficher("*")
    afficher_ligne()