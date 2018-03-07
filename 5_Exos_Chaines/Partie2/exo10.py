"""Intercale les caractères de chaine_2 entre chaque caractère de chaine_1
On suppose que len(chaine_2) <= len(chaine_1)"""

"""
DEBUT
afficher("Entrez une chaîne : ")
lire(chaine_1)

chaine_2 = ""
TANTQUE chaine_2 == "" FAIRE
    afficher("Entrez une autre chaîne : ")
    lire(chaine_2)
FTANTQUE

res = ""
j = 0  # indice de parcours de chaine_2

POUR car DANS chaine_1 FAIRE
    res += car + chaine_2[j]
    j = (j + 1) % taille(chaine_2)
FPOUR

afficher_ligne(res)
FIN
"""

from outils import *

afficher("Entrez une chaîne : ")
chaine_1 = lire_chaine()

chaine_2 = ""
while chaine_2 == "":
    afficher("Entrez une autre chaîne : ")
    chaine_2 = lire_chaine()

res = ""
j = 0  # indice de parcours de chaine_2
for car in chaine_1:
    res += car + chaine_2[j]
    j = (j + 1) % len(chaine_2)

afficher_ligne(res)
