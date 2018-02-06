"""Multiplication par additions successives
   On suppose ici que les deux opérandes sont positives ou nulles"""

from outils import *

# On fait sentir qu'un sous-progremme serait souhaitable pour encapsuler
# cette opération qui revient souvent...
nbre1 = -1
while nbre1 < 0:
    afficher("Entrez un nombre >= 0 : ")
    nbre1 = lire_nombre()

nbre2 = -1
while nbre2 < 0:
    afficher("Entrez un autre nombre >= 0 : ")
    nbre2 = lire_nombre()

resultat = 0
# Pour calculer nbre1 * nbre2, on effectue nbre2 fois le calcul
# nbre1 = nbre1 + nbre1
for _ in range(nbre2):
    resultat = resultat + nbre1

afficher_ligne(nbre1, "*", nbre2, "=", resultat)
