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


# On traite à part la cas où l'un des opérandes est nul
if nbre1 == 0 or nbre2 == 0:
    resultat = 0

# Si on voulait traiter les nombres négatifs, il faudrait isoler le signe
# du produit, travailler avec les valeurs absolues et remettre le signe au
# résultat

# Pour calculer nbre1 * nbre2, on effectue nbre2 - 1 fois le calcul
# nbre1 = nbre1 + nbre1

else:
    resultat = nbre1
    for _ in range(nbre2 - 1):
        resultat = resultat + nbre1

afficher_ligne(nbre1, "*", nbre2, "=", resultat)
