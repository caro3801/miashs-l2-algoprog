"""Volume d'un parallélépipède rectangle"""

from outils import *

afficher("Entrez la longueur : ")
longueur = lire_nombre()
afficher("Entrez la largeur : ")
largeur = lire_nombre()
afficher("Entrez la hauteur : ")
hauteur = lire_nombre()

volume = longueur * largeur * hauteur
afficher_ligne("Le volume du parallélépipède est", volume, "unités au cube")
