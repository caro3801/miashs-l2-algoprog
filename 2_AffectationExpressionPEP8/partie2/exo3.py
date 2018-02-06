"""Distributeur de billets"""

from outils import *

montant = 1
while montant % 10 != 0:    # Le retrait doit être multiple de 10
    afficher("Entrez le montant du retrait : ")
    montant = lire_nombre()

# Calcul du nombre de billets à distribuer : on commence par les plus gros
nb_50 = montant // 50
montant = montant % 50
nb_20 = montant // 20
montant = montant % 20
nb_10 = montant // 10

# Distribution des billets
if nb_50 != 0:
    afficher_ligne("Distribution de", nb_50, "billet(s) de 50€")
if nb_20 != 0:
    afficher_ligne("Distribution de", nb_20, "billet(s) de 20€")
if nb_10 != 0:
    afficher_ligne("Distribution de", nb_10, "billet(s) de 10€")
