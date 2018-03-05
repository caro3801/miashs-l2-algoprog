"""Déterminer si un nombre saisi est pair ou impair"""

"""
DEBUT
afficher("Entrez un nombre : ")
lire_nombre(nb)

SI nb % 2 == 0 ALORS
    afficher(nb,"est pair")
SINON
    afficher(nb,"est impair")
FSI

FIN
"""

from outils import *

afficher("Entrez un nombre : ")
nbre = lire_nombre()

# Méthode "classique"
if nbre % 2 == 0:
    afficher_ligne(nbre, "est pair")
else:
    afficher_ligne(nbre, "est impair")

# Méthode optimisée : un nombre est pair si le bit de poids faible de sa
# représentation binaire est 0
if nbre & 1 == 0:
    afficher_ligne(nbre, "est pair")
else:
    afficher_ligne(nbre, "est impair")
