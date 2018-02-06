""" indique si un nombre de 4 ou 5 chiffres donné par l'utilisateur
est un palindrome """
from outils import *

nombre = 1111111
while (nombre <= 999) or (nombre > 99999):
    afficher("donnez un nombre de 4 ou 5 chiffres : ")
    nombre = lire_nombre()

# Evaluation du nombre de chiffres : 4 ou 5 ?
if (nombre // 10000) != 0:
    # 5 chiffres
    div = 10000
else:
    # 4 chiffres
    div = 1000

# Test palindrome
palin = True
n = nombre
while (div >= 10) and palin:
    # on compare les chiffres situés aux extrémités du nombre
    # chiffre à gauche : n // div
    # chiffre à droite : n % 10
    if n // div != n % 10:
        palin = False
    # on passe au traitement des autres chiffres du nombre
    n = (n % div) // 10
    div = div // 100
if palin:
    afficher_ligne(nombre, " est un palindrome")
else:
    afficher_ligne(nombre, " n'est pas un palindrome")
