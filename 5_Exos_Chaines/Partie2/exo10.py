"""Intercale les caractères de chaine_2 entre chaque caractère de chaine_1
On suppose que len(chaine_2) <= len(chaine_1)"""

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
