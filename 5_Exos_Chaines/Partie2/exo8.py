"""Remplacement d'un caractère dans une chaîne...
   ATTENTION : En Python, les chaînes sont immuables, donc on ne peut pas
   remplacer les caractères individuellement. Il faut construire une nouvelle
   chaîne.
"""

"""
DEBUT
afficher("Entrez une chaîne : ")
lire(chaine)

new_chaine = ""
i = 0
TANTQUE i < taille(chaine) FAIRE
    new_chaine += chaine[i] + "*"
    i += 1
FTANQUE

******* OU ****
POUR car DANS chaine FAIRE
    new_chaine = new_chaine + car + "*"
FPOUR
******

afficher_ligne(new_chaine)

FIN
"""

from outils import *

afficher("Entrez une chaîne : ")
chaine = lire_chaine()

new_chaine = ""
for car in chaine:
    new_chaine = new_chaine + car + "*"

afficher_ligne(new_chaine)
