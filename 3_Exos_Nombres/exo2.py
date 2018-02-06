"""Calcul de la moyenne de 5 nombres saisis par l'utilisateur"""
from outils import *

NB_NOMBRES = 5
somme = 0

afficher_ligne("Entrez", NB_NOMBRES, "nombres :")
for i in range(1, NB_NOMBRES + 1):
    afficher("Nombre", i, ": ")
    nbre = lire_nombre()
    somme = somme + nbre   # ou : somme += nbre

moyenne = somme / NB_NOMBRES

afficher_ligne("La moyenne de ces", NB_NOMBRES, "nombres = ",
               round(moyenne, 2))
