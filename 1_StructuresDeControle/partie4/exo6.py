""" Calcul et affichage de la table de multiplication par 5"""

from outils import *

# On utilise une constante pour faciliter l'adaptation du programme
MULTIPLE = 5

produit = MULTIPLE
for nbre in range(1, 11):
    afficher_ligne(nbre, "x", MULTIPLE, " = ", produit)
    produit = produit + MULTIPLE