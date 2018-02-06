"""programme qui calcule et affiche les multiples de 7 compris entre 1 et 100"""

from outils import *

# Utilisation de constantes pour adaptation du programme et lisibilité
MUL = 7
MIN = 1
MAX = 100

multiple = MUL     # Premier multiple de MUL
while multiple in range(MIN, MAX + 1):
    afficher(multiple, " ")
    multiple = multiple + MUL

afficher_ligne()