from outils import *

afficher("Entrez une chaine de caractere : ")
phrase = lire_chaine()
cpt = phrase.count(" ")

afficher("Il y a ",cpt-1,"mots dans ", phrase)