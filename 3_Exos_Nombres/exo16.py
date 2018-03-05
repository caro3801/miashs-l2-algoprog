"""calculer les racines d'une équation du second degré."""
"""
DEBUT
afficher_ligne("Résolution de l'équation ax^2 + bx + c = 0")
afficher("Entrez le coefficient a : ")
lire(a)
afficher("Entrez le coefficient b : ")
lire(b)
afficher("Entrez le coefficient c : ")
lire(c)


delta = (b ** 2) - (4 * a * c)

SI delta > 0 ALORS
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    afficher("Deux racines :", x1, "et ", x2)
SINON SI delta == 0 ALORS
    x = -b / (2 * a)
    afficher("Une racine double :", x)
SINON
    afficher("Pas de racine dans R")
FSI

FIN
"""
from outils import *
import math

afficher_ligne("Résolution de l'équation ax^2 + bx + c = 0")
afficher_ligne("")

# Saisie des coefficients
afficher("Entrez le coefficient a : ")
a = lire_nombre()
afficher("Entrez le coefficient b : ")
b = lire_nombre()
afficher("Entrez le coefficient c : ")
c = lire_nombre()

# Calcul du discriminant
delta = (b ** 2) - (4 * a * c)

# Calcul des racines (on suppose a != 0)...
# Amélioration possible : prise en compte de a = 0, b = 0, c = 0
if delta > 0:
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print("Deux racines :", x1, "et ", x2)
elif delta == 0:
    x = -b / (2 * a)
    print("Une racine double :", x)
else:
    print("Pas de racine dans R")
