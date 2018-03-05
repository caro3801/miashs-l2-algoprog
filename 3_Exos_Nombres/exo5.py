"""Déterminer si un nombre saisi est un multiple de 5"""

"""
DEBUT
afficher("Entrez un nombre : ")
lire_nombre(nb)

SI nb % 5 == 0 ALORS
    afficher(nb,"est un multiple de 5")
SINON
    afficher(nb,"n'est pas un multiple de 5")
FSI

FIN
"""


from outils import *

afficher("Entrez un nombre : ")
nbre = lire_nombre()

if nbre % 5 == 0:
    afficher_ligne(nbre, "est un multiple de 5")
else:
    afficher_ligne(nbre, "n'est pas un multiple de 5")
