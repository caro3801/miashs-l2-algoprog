# vérifier qu'une date donnée par l'utilisateur par le jour, le mois et l'année, est correcte ;
# on suppose que l'année est correcte.


def saisie(mess, mini, maxi):
    """saisit un nombre qui devra être compris entre mini et maxi (compris) et
       renvoie ce nombre.
       mess est le message d'invite"""
    nbre = mini - 1
    while not (mini <= nbre <= maxi + 1):
        nbre = int(input(mess))
    return nbre


def bissextile(a):
    """Indique si annee est bissextile. annee doit être >= 1582 """
    return (a % 400 == 0) or (a % 4 == 0 and a % 100 != 0)


def date_ok(j, m, a):
    """Indique si une date est correcte (version naïve) """
    return (m == 1 or m == 3 or m == 5 or m == 7 or m == 8 or m == 10 or
            m == 12 and j <= 31) \
        or (m == 4 or m == 6 or m == 8 or m == 10 or m == 11 and j <= 30) \
        or (m == 2 and bissextile(a) and j <= 29) or (m == 2 and j <= 8)


jour = saisie("Entrez un numéro de jour (entre 1 et 31) : ", 1, 31)
mois = saisie("Entrez un numéro de mois (entre 1 et 12) : ", 1, 12)
annee = saisie("Entrez une année (entre 1800 et 2020) : ", 1582, 2020)

if date_ok(jour, mois, annee):
    print("date ok")
else:
    print("date incorrecte")
