"""compter le nombre de mots dans une chaine ;
la chaine est donnée par l'utilisateur,
les mots sont séparés par un espace."""

"""
DEBUT
afficher("Entrez une chaine de caractere : ")
lire(phrase)
cpt = 0
POUR car DANS phrase FAIRE
    SI car == " " ALORS
        cpt += 1
    FSI
FPOUR
afficher("Il y a ",cpt,"mots dans ", phrase)
FIN
"""

from outils import *

afficher("Entrez une chaine de caractere : ")
phrase = lire_chaine()
cpt = 0
for car in phrase:
    if car == " ":
        cpt += 1

afficher("Il y a ", cpt, "mots dans ", phrase)
