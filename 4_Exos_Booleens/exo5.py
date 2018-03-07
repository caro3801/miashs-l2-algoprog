"""demander deux nombres à l’utilisateur et déterminer si leur produit est négatif ou positif (on laisse de côté le cas
où le produit est nul) (on ne doit pas calculer le produit des deux nombres)."""
"""
DEBUT
afficher("N1 : ")
lire(n1)
afficher("N2 : ")
lire(n2)
SI n1 > 0 et n2 > 0 ALORS
    afficher("Le produit de", n1," et ",n2," est positif")
SINON SI n1 < 0 ou n2 < 0
    afficher("Le produit de", n1," et ",n2," est negatif")
FSI
FIN
"""

n1 = int(input("N1:"))
n2 = int(input("N2:"))

if n1 > 0 and n2 > 0:
    print("Le produit de", n1, " et ", n2, " est positif")
elif n1 < 0 or n2 < 0:
    print("Le produit de", n1, " et ", n2, " est negatif")
