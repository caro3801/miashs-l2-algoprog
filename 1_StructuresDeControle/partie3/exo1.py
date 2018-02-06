"""demande son âge à l'utilisateur et affiche s'il est 
mineur ou majeur suivant le cas"""

from outils import *

afficher("Quel âge as-tu ? ")
age = lire_nombre()
if age < 18:
	afficher_ligne("tu es mineur")
else: 
	afficher_ligne("tu es majeur")
