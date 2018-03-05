""" Obtention du L1 par un étudiant à partir de sa moyenne au semestre 1 et
au semestre 2.
Si l'étudiant n'a pas obtenu son L1, afficher s'il a obtenu le semestre 1 ou
le semestre 2"""

"""
DEBUT
afficher("Entrez la moyenne du S1 : ")
lire(moy_S1)
afficher("Entrez la moyenne du S2 : ")
lire(moy_S2)

if (moy_S1 + moy_S2) / 2 < 10:
    # L'étudiant n'a pas obtenu le L1
    # On suppose que l'obtention du L2 n'est pas liée à celle du L1 (?)
    afficher_ligne("\tL1 non obtenu :")
    SI moy_S1 < 10 ALORS
        afficher_ligne("\t- S1 non obtenu")
    SINON
        afficher_ligne("- S1 obtenu")
    FSI

    SI moy_S2 < 10 ALORS
        afficher_ligne("\t- S2 non obtenu")
    SINON
        afficher_ligne("\t- S2 obtenu")
    FSI

SINON
    # L'étudiant a obtenu sa L1
    afficher_ligne("L1 obtenue")
FSI
FIN
"""


from outils import *

afficher("Entrez la moyenne du S1 : ")
moy_S1 = lire_nombre()
afficher("Entrez la moyenne du S2 : ")
moy_S2 = lire_nombre()

if (moy_S1 + moy_S2) / 2 < 10:
    # L'étudiant n'a pas obtenu le L1
    # On suppose que l'obtention du L2 n'est pas liée à celle du L1 (?)
    afficher_ligne("\tL1 non obtenu :")
    if moy_S1 < 10:
        afficher_ligne("\t- S1 non obtenu")
    else:
        afficher_ligne("- S1 obtenu")
    if moy_S2 < 10:
        afficher_ligne("\t- S2 non obtenu")
    else:
        afficher_ligne("\t- S2 obtenu")
else:
    # L'étudiant a obtenu son L1
    afficher_ligne("L1 obtenu")
