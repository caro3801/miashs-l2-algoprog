""" Ecrire un programme qui demande l’âge d’un enfant à l’utilisateur et
    l’informe de sa catégorie : """

from outils import *

age = -1
while age not in range(6, 19):
    afficher("Entrez un âge compris entre 6 et 18 ans : ")
    age = lire_nombre()

if 6 <= age <= 8:          # ou : if age >= 6 and age <= 7
    afficher_ligne("Poussin")
elif 8 <= age < 10:
    afficher_ligne("Pupille")
elif 10 <= age < 12:
    afficher_ligne("Minime")
else:
    afficher_ligne("Cadet")
