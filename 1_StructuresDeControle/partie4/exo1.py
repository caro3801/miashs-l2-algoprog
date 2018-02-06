""" Ecrire un programme qui affiche le signe d'un nombre donné par
   l'utilisateur"""

from outils import *

afficher("Entrez un nombre : ")
nbre = lire_nombre()
if nbre < 0:
    afficher_ligne(nbre, "est strictement négatif")
elif nbre == 0:
    afficher_ligne(nbre, "est nul")
else:
    afficher_ligne(nbre, "est strictement positif")
