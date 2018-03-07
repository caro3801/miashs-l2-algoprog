"""une date donnée par l'utilisateur par le jour, le mois et l'année, est correcte ;
on suppose que l'année est correcte.
"""
"""
DEBUT
afficher("Donner une date")
afficher("jour")
lire(jour)
afficher("mois")
lire(mois)
afficher("année")
lire(annee)
bissextile = False
date_OK = True
SI annee %4 == 0 or annee% 100 and not annee % 400 ==0 ALORS
    bissextile = True

SI mois >=1 and mois <=12
    SI mois==2
        SI bissextile
            date_OK = 1 <= jour <=28
        SINON
            date_OK = 1 <= jour <=29
    SINON SI mois%2==0
        date_OK = 1 <= jour <=30
    SINON
        date_OK = 1 <= jour <=30
SINON
    date_OK = False
FSI

FIN
"""

print("Donner une date")
jour = int(input("jour : "))
mois = int(input("mois : "))
annee = int(input("année : "))

bissextile = False
date_OK = True
if (annee % 4 == 0 and not annee % 100) or (annee % 400 == 0):
    bissextile = True

if 1 <= mois <= 12:
    if mois == 2:
        if bissextile:
            date_OK = 1 <= jour <= 28
        else:
            date_OK = 1 <= jour <= 29
    elif mois % 2 == 0:
        date_OK = 1 <= jour <= 30
    else:
        date_OK = 1 <= jour <= 30
else:
    date_OK = False

if date_OK:
    print("date valide")
else:
    print("date invalide")
