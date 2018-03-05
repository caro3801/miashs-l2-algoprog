"""Jeu de dés : le programme simule deux joueurs qui lancent trois fois
   un dé chacun à leur tour.
   La somme des lancers est calculée pour chaque joueur.
"""
"""
DEBUT
encore = "O"
TANTQUE encore == "O" FAIRE
    somme1 = somme2 = 0

    POUR _ allant de 0 à 3 non compris FAIRE
        afficher("\nJe joue...")
        de = aleatoire(1, 6)
        afficher(de)
        somme1 += de
        afficher("\nA toi...")
        de = aleatoire(1, 6)
        afficher(de)
        somme2 += de
    FPOUR

    afficher_ligne("\n\nMon Total =", somme1)
    afficher_ligne("Ton Total =", somme2)

    SI somme2 > somme1 ALORS
        afficher_ligne("J'ai perdu")
    SINON SI somme1 > somme2 ALORS
        afficher_ligne("J'ai gagné")
    SINON
        afficher_ligne("ex-aequo")
    FSI

    afficher("Encore (o/n) ? ")
    lire(encore)
FTANTQUE

FIN
"""
from outils import *

encore = "O"
while encore == "O":
    somme1 = somme2 = 0

    for _ in range(3):
        afficher("\nJe joue...")
        de = aleatoire(1, 6)
        afficher(de)
        somme1 += de
        afficher("\nA toi...")
        de = aleatoire(1, 6)
        afficher(de)
        somme2 += de

    afficher_ligne("\n\nMon Total =", somme1)
    afficher_ligne("Ton Total =", somme2)

    if somme2 > somme1:
        afficher_ligne("J'ai perdu")
    elif somme1 > somme2:
        afficher_ligne("J'ai gagné")
    else:
        afficher_ligne("ex-aequo")

    encore = input("Encore (o/n) ? ").upper()
