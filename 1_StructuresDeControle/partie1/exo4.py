"""Écrire un programme qui saisit un nombre entier positif ou nul et qui
   affiche autant de *"""

from outils import *

nb = -1
while nb < 0:
    afficher("Entrez un entier positif ou nul : ")
    nb = lire_nombre()

# Pour être sûr que nb est bien un entier et pas un réel :
nb = int(nb)

# Affiche nb astérisques  (Rque: un simple afficher_ligne("*" * nb) suffirait..
#                                voir aussi exo8bis
for _ in range(nb):
    afficher("*")

afficher_ligne()
