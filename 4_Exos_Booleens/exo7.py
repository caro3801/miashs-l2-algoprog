""" demander 2 bornes entières, additionner les entiers entre ces 2 bornes,
multiples de 3 ou de 5 ; afficher le résultat. """
"""
DEBUT
afficher("Entrez la première borne : ")
lire(borne_1)
afficher("Entrez la deuxième borne : ")
lire(borne_2)

afficher("Les multiples de 3 ou 5 compris entre", borne_1, "et", borne_2, "sont : ")

POUR nbre allant de borne_1 à borne_2 comprise FAIRE
    SI nbre % 3 == 0 ou nbre % 5 == 0 ALORS
        afficher(nbre, " ")
    FSI
FPOUR

FIN
"""

from outils import *

afficher("Entrez la première borne : ")
borne_1 = int(lire_nombre())
afficher("Entrez la deuxième borne : ")
borne_2 = int(lire_nombre())

# Comme on parcourt tous les entiers de borne_1 à borne_2, c'est une boucle for
afficher("Les multiples de 3 ou 5 compris entre", borne_1, "et", borne_2,
         "sont : ")
for nbre in range(borne_1, borne_2 + 1):
    if nbre % 3 == 0 or nbre % 5 == 0:
        afficher(nbre, " ")

# Retour à la ligne final
afficher_ligne()
