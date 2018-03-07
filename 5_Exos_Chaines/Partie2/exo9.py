"""Remplacement d'un caractère dans une chaîne...
   ATTENTION : En Python, les chaînes sont immutables, donc on ne peut pas
   remplacer les caractères individuellement. Il faut construire une nouvelle
   chaîne.
"""
"""
DEBUT
afficher("Entrez une chaîne : ")
chaine = lire_chaine()
afficher("Entrez un caractère à remplacer : ")
ancien = lire_chaine()
afficher("Entrez le caractère de remplacement : ")
nouveau = lire_chaine()

new_chaine = ""
i = 0
TANTQUE i < taille(chaine) FAIRE
    car = chaine[i]
    SI car == ancien ALORS
        car = nouveau
    FSI
    new_chaine += car
    i += 1
FTANQUE


afficher_ligne(new_chaine)

FIN
"""
from outils import *

afficher("Entrez une chaîne : ")
chaine = lire_chaine()
afficher("Entrez un caractère à remplacer : ")
ancien = lire_chaine()
afficher("Entrez le caractère de remplacement : ")
nouveau = lire_chaine()

new_chaine = ""
for i in range(len(chaine)):
    car = chaine[i]
    if chaine[i] == ancien:
        car = nouveau

    new_chaine += nouveau

afficher_ligne(new_chaine)
