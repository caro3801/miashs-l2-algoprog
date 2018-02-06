"""Compte le nombre d'entiers supérieurs à 10 entre 1 et 10 non compris"""

from outils import *

compte = 0
i = 1
while i < 10:
    compte = compte + 1
    i = i + 1 
afficher_ligne(compte)


"""Remarque: l'algo était conceptuellement faux puisqu'il s'agissait d'un
pour et non d'un tant que...
Et, perso, je ne vois pas trop son intérêt...

compte = 0
for _ in range(10):
   compte = compte + 1
"""