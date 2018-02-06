"""Remplacement d'un caractère dans une chaîne...
   ATTENTION : En Python, les chaînes sont immutables, donc on ne peut pas
   remplacer les caractères individuellement. Il faut construire une nouvelle
   chaîne.
"""
from outils import *

afficher("Entrez une chaîne : ")
chaine = lire_chaine()
afficher("Entrez un caractère à remplacer : ")
ancien = lire_chaine()
afficher("Entrez le caractère de remplacement : ")
nouveau = lire_chaine()

new_chaine = ""
for car in chaine:
    if car == ancien:
        new_chaine = new_chaine + nouveau
    elif car == nouveau:
        new_chaine = new_chaine + ancien
    else:
        new_chaine = new_chaine + car

afficher_ligne(new_chaine)
