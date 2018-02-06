"""calcule et affiche un nombre à la puissance n, le nombre et n étant donnés 
par l'utilisateur"""

from outils import *
 
afficher("Donnez un nombre : ")
nbre = lire_nombre()
afficher("Donnez la puissance : ")
exposant = lire_nombre()
resultat = 1

for _ in range(exposant):
	resultat = resultat * nbre
    
afficher_ligne("le nombre ", nbre,"à la puissance ", exposant, "vaut : ", resultat)
