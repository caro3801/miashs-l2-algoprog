"""Calcul du nombre de grains de riz sur un échiquier selon la légende de Sissa
Voir https://fr.wikipedia.org/wiki/Histoire_du_jeu_d%27échecs.
Le nombre de grains de riz est égal à 2^0 + 2^1 + 2^2 + ... 2^63"""

"""
DEBUT
somme = 0
Pour i allant de 0 à 64 non compris FAIRE
    somme = somme + 2 ** i
FPOUR

afficher_ligne(somme)
FIN
"""


from outils import afficher_ligne
somme = 0
for i in range(64):
    somme = somme + 2 ** i

afficher_ligne(somme)

# Autre façon de procéder (plus efficace)...
# On sait que 2^0 + 2^1 + 2^2 + ... 2^63 = 2^64 - 1

somme = 2 ** 64 - 1
afficher_ligne(somme)

# On peut même se passer de somme si on ne l'utilise que pour l'afficher
afficher_ligne(2 ** 64 - 1)
