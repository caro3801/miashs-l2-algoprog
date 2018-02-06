"""Calcul de la moyenne pondérés de 3 nombres"""
from outils import *

NB_NOMBRES = 3
somme = 0
total_pond = 0

afficher_ligne("Entrez", NB_NOMBRES, "nombres :")
for i in range(1, NB_NOMBRES + 1):
    afficher("Nombre", i, ": ")
    nbre = lire_nombre()
    afficher("Pondération", i, ": ")
    pond = lire_nombre()
    somme = somme + nbre * pond      # ou : somme += nbre * pond
    total_pond = total_pond + pond   # ou : total_pond += pond

moyenne = somme / total_pond

afficher_ligne("La moyenne de ces", NB_NOMBRES, "nombres = ",
               round(moyenne, 2))
