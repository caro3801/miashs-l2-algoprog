"""Affiche la liste des nbrs parfaits inférieurs à une limite donnée"""
from math import sqrt
from outils import *

# Saisie de la limite
limite = 0
while limite < 2:
    afficher("Entrez une limite >= 2 : ")
    limite = int(lire_nombre())

# Boucle de recherche des nombres parfaits <= limite
for nbre in range(2, limite + 1):
    # Calcul de la somme des div propres de nbre
    somme = 1
    root = int(sqrt(nbre))
    for div in range(2, root + 1):
        if nbre % div == 0:
            somme = somme + div + (nbre // div)
        if nbre == root * root:
            somme = somme - root

    # nbre est parfait si nbre == somme de ses div propres
    if nbre == somme:
        afficher(nbre, " ")

afficher_ligne()
