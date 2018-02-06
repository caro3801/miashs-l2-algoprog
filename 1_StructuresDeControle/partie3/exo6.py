""" calcule et affiche le nombre de diviseurs propres d'un nombre donné 
par l'utilisateur"""

from outils import *
 
afficher("Donnez un entier : ")
nbre = lire_nombre()
diviseur = 1
cpteur = 0
while diviseur < nbre:
	if nombre % diviseur == 0:
		cpteur = cpteur + 1
	diviseur = diviseur + 1
afficher_ligne("le nombre de diviseurs propres de ", nbre," est : ", cpteur)

"""Remarques :

- Du dégât de choisir des noms de variables fantaisistes...
- l'algo était faux car le while aurait dû être un pour : 
nbre = lire_nombre()
cpteur = 0
for diviseur in range(1, nbre):
	if nombre % diviseur == 0:
		cpteur = cpteur + 1
afficher(...)
"""