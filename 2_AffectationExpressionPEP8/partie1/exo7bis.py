"""Simulation d'une calculatrice (version avec vérification de la saisie)"""

from outils import *

# Saisie de deux nombres
afficher("Saisir un nombre : ")
nb1 = lire_nombre()
afficher("Saisir un autre nombre : ")
nb2 = lire_nombre()

# Saisie d'un code opération
oper = " "
while oper != "+" and oper != "-" and oper != "*" and oper != "/":
    oper = input("Saisir une opération (+, -, * ou /) : ")

# Réalisation de l'opération
erreur = False
if oper == "+":
    resultat = nb1 + nb2
elif oper == "-":
    resultat = nb1 - nb2
elif oper == "*":
    resultat = nb1 * nb2
elif nb2 != 0:   # Ici, on a donc une division avec un diviseur non nul...
    resultat = nb1 // nb2
else:            # Ici, on a une division avec un diviseur nul...
    erreur = True

# Affichage du résultat
if not erreur:
    afficher_ligne("Le résultat de", nb1, oper, nb2, "=", resultat)
else:
    afficher_ligne("Erreur : la division par 0 n'est pas possible")
