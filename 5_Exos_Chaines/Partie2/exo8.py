"""Remplacement d'un caractère dans une chaîne...
   ATTENTION : En Python, les chaînes sont immutables, donc on ne peut pas
   remplacer les caractères individuellement. Il faut construire une nouvelle
   chaîne.
"""
from outils import *

afficher("Entrez une chaîne : ")
chaine = lire_chaine()

new_chaine = ""
for car in chaine:
    new_chaine = new_chaine + car + "*"

afficher_ligne(new_chaine)
