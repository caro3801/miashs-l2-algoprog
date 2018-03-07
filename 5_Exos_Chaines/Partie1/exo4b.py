"""
Donner l'indice le plus à droite d'un caractère ;
la chaine de caractères est donnée par l'utilisateur.
"""

"""
DEBUT
afficher("Entrez une chaine de caractere : ")
lire(phrase)
afficher("Quel caractere compter?  ")
lire(car)
i=0
TANTQUE i < taille(phrase) ET phrase[i] != car FAIRE
    i = i + 1
FTANTQUE

SI i == taille(phrase) ALORS
    afficher_ligne("L'indice le plus à droite est",i+1 % taille(phrase) )
SINON
    afficher_ligne("Le caractere n'a pas été trouvé")
FSI

FIN
"""

from outils import *

afficher("Entrez une chaîne : ")
chaine = lire_chaine()
afficher("Entrez un caractère : ")
car = lire_chaine()

i = 0
while i < len(chaine) and chaine[i] != car:
    i += 1
if i == len(chaine):
    afficher_ligne(car, "n'est pas dans", chaine)
else:
    afficher_ligne(car, "est à l'indice", i+1 % len(phrase))
