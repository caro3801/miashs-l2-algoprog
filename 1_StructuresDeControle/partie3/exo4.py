"""Fait la somme de dix nombres donnés par l'utilisateur et 
affiche le résultat"""

from outils import *

somme = 0
for i in range(1, 11):
	afficher("donnez le nombre numéro ", i, " : ")
	n = lire_nombre()
	somme = somme + n
afficher_ligne("la somme est égale à : ", somme)
