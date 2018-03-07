""" Obtention du L3 (il faut aussi la moyenne au stage pour l'obtention du S2)"""

from outils import *


def semestreObtenu(semestre, moy):
    obtenu = False
    if moy < 10:
        afficher_ligne("\t- ", semestre, " non obtenu")
        obtenu = True
    else:
        afficher_ligne("\t- ", semestre, " obtenu")
    return obtenu


def anneeObtenue(niveau, stage=False):
    afficher_ligne("Résultats de ", niveau, " : ")
    sem1 = "S" + str(int(niveau[1]) * 2 - 1)
    sem2 = "S" + str(int(niveau[1]) * 2)
    afficher("Entrez la moyenne du ", sem1, " : ")
    moy_S1 = lire_nombre()
    afficher("Entrez la moyenne du ", sem2, " : ")
    moy_S2 = lire_nombre()
    pas_obtenu = (moy_S1 + moy_S2) / 2 < 10

    if stage:
        afficher("Entrez la moyenne du stage S2 : ")
        moy_stage_S2 = lire_nombre()
        pas_obtenu = moy_stage_S2 < 10 or (moy_S1 + moy_S2) / 2 < 10

    if pas_obtenu:
        # L'étudiant n'a pas obtenu le L1
        # On suppose que l'obtention du L2 n'est pas liée à celle du L1 (?)
        afficher_ligne("\t", niveau, " non obtenue :")
        semestreObtenu(sem1, moy_S1)

        semestreObtenu(sem2, moy_S2)

        if stage:
            semestreObtenu("stage", moy_stage_S2)
    else:
        # L'étudiant a obtenu son L1
        afficher_ligne(niveau, " obtenue")


anneeObtenue("L1")
anneeObtenue("L2", True)
anneeObtenue("L3")
