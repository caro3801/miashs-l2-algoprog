"""calculer le nombre de multiples de 7 parmi 10 entiers donnés par l'utilisateur"""

"""
DEBUT
afficher("donner 10 entiers")
cpt = 0
POUR i allant de 0 à 10 non compris FAIRE
    afficher("Entier",i,":")
    lire(nb)
    SI nb % 7 == 0 ALORS
        afficher(nb, "est un multiple de 7")
        cpt += 1
    SINON
        afficher(nb, "n'est pas un multiple de 7")
FPOUR
afficher ("vous avez saisi", cpt, "multiples de 7")

FIN
"""


print("donner 10 entiers")
cpt = 0
for i in range(10) :
    nb  = int(input("Entier",i,":"))
    if nb % 7 == 0 :
        print(nb, "est un multiple de 7")
        cpt += 1
    else :
        print(nb, "n'est pas un multiple de 7")

print("vous avez saisi", cpt, "multiples de 7")
