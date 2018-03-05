"""déterminer si un nombre donné par l'utilisateur est premier"""

"""
DEBUT
afficher("donner un nombre")
lire(nb)
i=2
premier = VRAI
TANTQUE i < nb ET premier FAIRE
    SI nb % i == 0 ALORS
        premier = FAUX
    i += 1
FTANQUE

SI premier ALORS
    afficher(nb,"est premier")
SINON
    afficher(nb,"n'est pas premier")
FSI
FIN
"""

nb = int(input("donner un nombre"))
i=2
premier = True
while i < nb and premier:
    if nb % i == 0:
        premier = False
    i += 1

if premier:
    print(nb,"est premier")
else :
    print(nb,"n'est pas premier")
