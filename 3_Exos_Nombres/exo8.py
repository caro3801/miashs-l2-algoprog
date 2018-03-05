""" Calculer la factorielle d'un nombre donné par l'utilisateur """
"""
!5 = 5*4*3*2*1
DEBUT
afficher("donner un nombre pour calculer sa factorielle")
lire(factorielle)
res = 1

POUR i allant de factorielle à 0 non compris en -1 faire
    res = res * i     # res *= i
FPOUR
afficher(res)
FIN
"""

"""
DEBUT
afficher("donner un nombre pour calculer sa factorielle")
lire(factorielle)
res = 1

TANT QUE factorielle >0 FAIRE
    res = res * factorielle
    factorielle = factorielle - 1
FTANT QUE
afficher(res)
FIN
"""

print("donner un nombre pour calculer sa factorielle")
factorielle = int(input())
res = 1

while (factorielle > 0) :
    res = res * factorielle
    factorielle = factorielle - 1

print("Résultat de la factorielle de ", factorielle,":",res)