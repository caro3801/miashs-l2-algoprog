# calcule et affiche le plus grand de cinq nombres donnés par l'utilisateur

from outils import *
 
afficher("Donnez un nombre : ")
x = lire_nombre()
max = x
i = 1
while i <= 4:
	afficher("donnez un nombre ")
	x = lire_nombre()
	if x > max:
		max = x
	i = i + 1
afficher_ligne("le nombre le plud grand est : ", max)


"""Même remarque: l'algo était faux : le while est un for :

afficher("Donnez un nombre : ")
x = lire_nombre()
max = x
for _ in range(4):
	afficher("donnez un nombre ")
	x = lire_nombre()
	if x > max:
		max = x
afficher_ligne("le nombre le plud grand est : ", max)
"""