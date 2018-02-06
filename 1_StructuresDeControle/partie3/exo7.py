"""Calcule et affiche combien parmi dix  nombres donnés par l'utilisateur 
sont supérieurs à 10"""

from outils import *
 
cpt = 0
for i in range(1, 11):
	afficher("donnez un nombre ")
	n = lire_nombre()
	if n > 10:
		cpt = cpt + 1
afficher_ligne(cpt, "nombres sont supérieurs à 10")
