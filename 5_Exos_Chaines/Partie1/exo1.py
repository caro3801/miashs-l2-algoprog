from outils import *

afficher("Entrez une phrase : ")
phrase = lire_chaine()
for car in phrase:
    afficher(car + " ")
afficher_ligne()
