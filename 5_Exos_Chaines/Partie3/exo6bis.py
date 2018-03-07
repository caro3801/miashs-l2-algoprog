from outils import *

voyelles = "aeiouyAEIOUY"
cpt = 0

afficher("Entrez une chaine de caracteres : ")
phrase = lire_chaine()

for car in voyelles:
    cpt += phrase.count(car)

afficher("il y a ",cpt," voyelle(s) dans ",phrase)