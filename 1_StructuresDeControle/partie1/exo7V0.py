"""Calcule et affiche les multiples de 7 compris entre 1 et 100"""

from outils import *

multiple = 7     # Premier multiple de 7
while multiple in range(1, 101):
    afficher(multiple, " ")
    multiple = multiple + 7

afficher_ligne()
