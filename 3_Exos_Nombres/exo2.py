"""Calcul de la moyenne de 5 nombres saisis par l'utilisateur"""

"""
DEBUT
NB_NOMBRES = 5
somme = 0
POUR i allant de 1 à NB_NOMBRES+1 FAIRE
    afficher("Nombre",i,":")
    lire(nb)
    somme+=nb
FPOUR
moy = somme / NB_NOMBRES
afficher("moyenne des ",NB_NOMBRES," nombres : ",moy)
FIN
"""

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
