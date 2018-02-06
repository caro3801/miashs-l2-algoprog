"""Multiplication par additions successives
   Version prenant en compte le signe"""

from outils import *

afficher("Entrez un nombre : ")
nbre1 = lire_nombre()
nbre1 = int(nbre1)             # Au cas où on aurait saisi un réel

afficher("Entrez un autre nombre : ")
nbre2 = lire_nombre()
nbre2 = int(nbre2)            # Au cas où on aurait saisi un réel

# On traite à part la cas où l'un des opérandes est nul
if nbre1 == 0 or nbre2 == 0:
    resultat = 0
else:
    # On détermine le signe du produit
    if (nbre1 > 0 and nbre2 > 0) or (nbre1 < 0 and nbre2 < 0):
        signe = 1
    else:
        signe = -1

    # Puis on travaille sur les valeurs absolues
    abs_nbre1 = abs(nbre1)
    abs_nbre2 = abs(nbre2)

    resultat = abs_nbre1
    for _ in range(abs_nbre2 - 1):
        resultat = resultat + abs_nbre1

    # On remet le signe
    resultat = signe * resultat


afficher_ligne(nbre1, "*", nbre2, "=", resultat)
