"""compter le nombre de voyelles dans une chaine de caractères ;
la chaine de caractères est donnée par l'utilisateur."""

"""
DEBUT
voyelles = "aeiouyAEIOUY"
afficher("Entrez une chaine de caractere : ")
lire(phrase)
POUR car DANS phrase FAIRE
    SI car in voyelles ALORS
        cpt = cpt +1
    FSI
FPOUR

afficher("il y a ",cpt," voyelles dans ",phrase)
FIN
"""

from outils import *
voyelles = "aeiouyAEIOUY"
afficher("Entrez une chaine de caracteres : ")
phrase = lire_chaine()
for car in phrase :
    if car in voyelles :
        cpt = cpt +1


afficher("il y a ",cpt," voyelle(s) dans ",phrase)