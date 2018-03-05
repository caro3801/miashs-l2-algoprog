"""Convertir une note donnée par l'utilisateur en appréciation (TB, B, ...)"""

"""
DEBUT
afficher("Donner la note")
lire(note)
appreciation = "Mauvaise saisie de la note"
SI 0<= note <= 20 ALORS
    SI 16 <= note <= 20 ALORS
        appreciation = "TB"
    SINON SI 14 <= note < 16 ALORS
        appreciation = "B"
    SINON SI 12 <= note < 14 ALORS
        appreciation = "AB"
    SINON SI 10 <= note < 12 ALORS
        appreciation = "Passable"
    SINON
        appreciation = "Non admis"
    FSI
    afficher("Avec", note, "votre appreciation est",appreciation)
SINON
    afficher(appreciation)
FSI
FIN
"""

note = float(input("Donner la note"))
appreciation = "Mauvaise saisie de la note"
if 0<= note <= 20 :
    if 16 <= note <= 20 :
        appreciation = "TB"
    elif 14 <= note < 16 :
            appreciation = "B"
    elif 12 <= note < 14 :
            appreciation = "AB"
    elif 10 <= note < 12 :
        appreciation = "Passable"
    else :
        appreciation = "Non admis"

    print("Avec", note, "votre appreciation est",appreciation)
else :
    print(appreciation)
