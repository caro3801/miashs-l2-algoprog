"""
Ecrire un programme qui affiche le signe d'un nombre donné par l'utilisateur
DEBUT
#initialisation
lire(nombre)

#calcul
Si nombre < 0 alors

    #affichage :
    afficher("negatif")

sinon
    #affichage :
    afficher("positif")
FSi

FIN

#Jeu d'essai : nombre
    {1} => Positif
    {0} => Positif
    {-1} => Négatif
"""
from outils import *

nombre = lire_nombre()

if nombre < 0:
    afficher("Négatif")
else:
    afficher("Positif")
