""" Décomposer un entier < 10000 saisi au clavier en milliers, centaines,
    dizaines et unités. Afficher le résultat """


def saisir(mess, limite):
    """Saisit un entier positif < limite"""
    nombre = -1
    while not (0 <= nombre < limite):
        saisie = input(mess)
        if saisie.isnumeric():
            nombre = int(saisie)
    return nombre


def decomposer(mil, cent, dix, unit):
    """Renvoie une chaîne contenant mil x 1000 + cent x 100 + ...
       Si l'un des paramètre est nul, il n'apparaît pas dans le résultat"""
    res = ""
    if mil != 0:
        res = res + str(mil) + " x 1000 + "
    if cent != 0:
        res = res + str(cent) + " x 100"
    if dix != 0:
        res = res + " + " + str(dix) + " x 10"
    if unit != 0:
        res = res + " + " + str(unit)
    return res


# Programme principal
nb = saisir("Entrez un nombre positif, strictement inférieur à 10000 : ", 10000)

# Décomposition de nb
milliers = nb // 1000
reste = nb - (milliers * 1000)
centaines = reste // 100
reste -= centaines * 100
dizaines = reste // 10
unites = reste - (dizaines * 10)

# Affichage du résultat
print(nb, "=", decomposer(milliers, centaines, dizaines, unites))
