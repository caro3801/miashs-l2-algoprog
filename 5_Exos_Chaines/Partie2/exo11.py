"""décoder une chaine qui a été codée suivant
 l'algorithme précédent. (intercalage de deux chaines)"""

"""
DEBUT

afficher("Entrez la chaîne à decoder : ")
lire(res)
chaine_1 = ""
chaine_2 = ""
i = 0
TANTQUE i < taille(res) FAIRE
    SI i % 2 == 0 ALORS
        chaine_1 += res[i]
    SINON
        chaine_2 += res[i]
    FSI
    i += 1
FTANQUE
afficher("Chaine1: ",chaine_1)
afficher("Chaine2: ",chaine_2)
FIN
"""

from outils import *

afficher("Entrez la chaîne à decoder : ")
res = lire_chaine()
chaine_1 = ""
chaine_2 = ""
i = 0
while i < len(res) :
    if i % 2 == 0 :
        chaine_1 += res[i]
    else:
        chaine_2 += res[i]

    i += 1

afficher("Chaine1: ",chaine_1)
afficher("Chaine2: ",chaine_2)