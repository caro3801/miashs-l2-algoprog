""" valider une saisie : demander une note à l'utilisateur ; si la note n'est pas comprise entre 0 et 20, recommencer."""
"""
DEBUT
afficher("donner une note")
lire(note)
TANTQUE NON (0 <= note <= 20) FAIRE
    afficher("mauvaise note, nouvelle saisie")
    lire(note)
FTANTQUE
FIN
"""

note = int(input("donner note"))
while not (0 <= note <= 20):
    note = int(input("nouvelle note"))
