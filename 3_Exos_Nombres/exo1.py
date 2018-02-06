"""Calcul du périmètre d'un rectangle"""
from outils import *

afficher("Entrez la longueur du rectangle : ")
longueur = lire_nombre()
afficher("Entrez sa largeur : ")
largeur = lire_nombre()

perimetre = 2 * (longueur + largeur)

afficher_ligne("Le périmètre de ce rectangle fait", perimetre, "unités.")
