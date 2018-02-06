"""Jeu du 421 simplifié :
    Le programme et le joueur lancent 3 dés chacun leur tour.
    Le premier qui fait la combinaison 421 a gagné
    Les combinaisons sont stockés dans une chaîne (pour simuler un tuple ou
    une liste)"""

from outils import *


def jouer(user):
    """Renvoie True si la combinaison de dés est 421"""
    combinaison = ""
    print(user, "joue...", end=" : ")
    for _ in range(3):
        de = str(aleatoire(1, 6))       # On convertit le chiffre en chaîne...
        print(de, end=" ")
        combinaison += de
    print()
    return "1" in combinaison and "2" in combinaison and "4" in combinaison


# Prog principal
nom = input("Bonjour, quel est ton nom ? ")

encore = "O"
while encore.upper() == "O":
    gagneOrdi = gagneUser = False
    while not gagneOrdi and not gagneUser:
        if not gagneUser:
            gagneOrdi = jouer("L'ordinateur")
        if not gagneOrdi:
            gagneUser = jouer(nom)

    if gagneOrdi:
        print("L'ordinateur a gagné..")
    else:
        print(nom, "a gagné...")

    encore = input("Encore ? ")
