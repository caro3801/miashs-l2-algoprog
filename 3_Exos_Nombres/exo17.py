"""Jeu de pierre-feuille-ciseaux"""
"""
DEBUT
encore = "O"
TANTQUE encore == "O" FAIRE
    choix_joueur = -1
    TANTQUE choix_joueur not in range(0, 3) FAIRE
        afficher("Choisissez : pierre (0), feuille (1) ou ciseaux (2) : ")
        lire(choix_joueur)
    FTANTQUE
    choix_prog = aleatoire(0, 2)

    SI choix_joueur == 0 ALORS
        afficher_ligne("Vous avez choisi la pierre...")
    SINON SI choix_joueur == 1 ALORS
        afficher_ligne("Vous avez choisi la feuille...")
    SINON
        afficher_ligne("Vous avez choisi les ciseaux...")
    FSI

    SI choix_prog == 0 ALORS
        afficher_ligne("Le programme a choisi la pierre...")
    SINON SI choix_prog == 1 ALORS
        afficher_ligne("Le programme a choisi la feuille...")
    SINON
        afficher_ligne("Le programme a choisi les ciseaux...")
    FSI

    SI choix_joueur == 0 ALORS     # Pierre
        if choix_prog == 0:
            res = "ex-aequo"
        SINON SI choix_prog == 1 ALORS
            res = "Perdu : la feuille enveloppe la pierre"
        SINON
            res = "Gagné : les ciseaux se cassent sur la pierre"
        FSI

    SINON SI choix_joueur == 1 ALORS   # Feuille
        SI choix_prog == 0 ALORS
            res = "Gagné : la feuille enveloppe la pierre"
        SINON SI choix_prog == 1 ALORS
            res = "ex-aequo"
        SINON
            res = "Perdu : les ciseaux coupent la feuille"
        FSI

    SINON                     # ciseaux
        if choix_prog == 0 ALORS
            res = "Perdu : les ciseaux se cassent sur la pierre"
        SINON SI choix_prog == 1 ALORS
            res = "Gagné : les ciseaux coupent la feuille"
        SINON
            res = "ex-aequo"
        FSI

    FSI
    afficher_ligne(res)

    afficher("Encore (o/n) ? ")
    lire(encore)
FTANTQUE

FIN
"""


from outils import *

encore = "O"
while encore == "O":
    choix_joueur = -1
    while choix_joueur not in range(0, 3):
        afficher("Choisissez : pierre (0), feuille (1) ou ciseaux (2) : ")
        choix_joueur = lire_nombre()
    choix_prog = aleatoire(0, 2)

    # On sent bien que les sous-programmes nous permettront d'alléger le code
    if choix_joueur == 0:
        afficher_ligne("Vous avez choisi la pierre...")
    elif choix_joueur == 1:
        afficher_ligne("Vous avez choisi la feuille...")
    else:
        afficher_ligne("Vous avez choisi les ciseaux...")

    if choix_prog == 0:
        afficher_ligne("Le programme a choisi la pierre...")
    elif choix_prog == 1:
        afficher_ligne("Le programme a choisi la feuille...")
    else:
        afficher_ligne("Le programme a choisi les ciseaux...")

    if choix_joueur == 0:     # Pierre
        if choix_prog == 0:
            res = "ex-aequo"
        elif choix_prog == 1:
            res = "Perdu : la feuille enveloppe la pierre"
        else:
            res = "Gagné : les ciseaux se cassent sur la pierre"
    elif choix_joueur == 1:   # Feuille
        if choix_prog == 0:
            res = "Gagné : la feuille enveloppe la pierre"
        elif choix_prog == 1:
            res = "ex-aequo"
        else:
            res = "Perdu : les ciseaux coupent la feuille"
    else:                     # ciseaux
        if choix_prog == 0:
            res = "Perdu : les ciseaux se cassent sur la pierre"
        elif choix_prog == 1:
            res = "Gagné : les ciseaux coupent la feuille"
        else:
            res = "ex-aequo"

    afficher_ligne(res)

    encore = input("Encore (o/n) ? ").upper()
