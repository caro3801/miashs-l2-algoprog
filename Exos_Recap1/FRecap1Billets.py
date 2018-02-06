# distributeur de billets avec max 2/3 de billets de 50 euros
from outils import *

somme = 1000
while (somme > 500) or ((somme % 10) != 0):
    afficher("donnez un montant (max. 500) : ")
    somme = lire_nombre()

# Nombre maximum de billets de 50
max_50 = (int)(somme * 2 / 3)

# Billets de 50
if (max_50 >= 50):
    nb_50 = max_50 // 50
    afficher_ligne(nb_50, " billets de 50 euros")
    somme = somme - (nb_50 * 50)
# Billets de 20
nb_20 = somme // 20
if nb_20 > 0:
    afficher_ligne(nb_20, " billets de 20 euros")
# Billets de 10
nb_10 = somme % 20
if nb_10 > 0:
    afficher_ligne(nb_10, " billets de 10 euros")
