"""afficher une chaine caractère par caractères ;
 la chaine de caractères est donnée par l'utilisateur."""
"""
DEBUT
afficher("Entrez une phrase : ")
lire(phrase)
POUR car DANS phrase FAIRE
    afficher(car + " ")
FPOUR
afficher_ligne()

FIN
"""

from outils import *

afficher("Entrez une phrase : ")
phrase = lire_chaine()
for car in phrase:
    afficher(car + " ")
afficher_ligne()
