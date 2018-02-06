"""Simulation d'une calculatrice (version avec vérification de la saisie)"""

from outils import *

# Saisie de deux nombres
afficher("Saisir un nombre : ")
nb1 = lire_nombre()
afficher("Saisir un autre nombre : ")
nb2 = lire_nombre()

# Saisie d'un code opération
oper = 0
while oper not in range(1, 5):   
    afficher("Saisir une opération (1 = +, 2 = -, 3 = * et 4 = /) : ")
    oper = lire_nombre()
    
# Réalisation de l'opération
erreur = False
if oper == 1:
    resultat = nb1 + nb2
elif oper == 2:
    resultat = nb1 - nb2
elif oper == 3:
    resultat = nb1 * nb2
else:
	if nb2 != 0:
		resultat = nb1 // nb2
	else:
		erreur = True
		afficher_ligne("erreur : la division par 0 n'est pas possible")
	

# Affichage du résultat
if not erreur:
	afficher_ligne("Le résultat de l'opération est ", resultat)
