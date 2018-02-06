""" demander l'année d'un événement (par exemple, l'année de naissance de
L. de Vinci : 1452) et afficher bravo si la date est correcte à 5 ans près """

from outils import *

# On stocke la bonne réponse dans une "constante"
REPONSE_OK = 1452

afficher("Quelle est l'année de naissance de Léonard de Vinci ? ")
date = lire_nombre()

if REPONSE_OK - 5 <= date <= REPONSE_OK + 5:
    afficher_ligne("Bravo")
else:
    afficher_ligne("Non, Léonard de Vinci est né en", REPONSE_OK)
