""" calculer le prix à payer à l'entrée de la piscine, connaissant les règles suivantes :
• enfants de moins de 7 ans : gratuit
• séniors (65 ans et plus): gratuit
• tarif réduit (toulousains de moins de 25 ans) : 1.40 €
• tarif normal : 3.40 €"""
"""
DEBUT
afficher("Quel age avez vous?")
lire(age)
afficher("Etes vous toulousains?(o=1/n=0)")
lire(toulousain)
SI age<7 OU age >= 65 ALORS
    afficher("gratuit")
SINON SI toulousain == 1 ET age < 25 ALORS
    afficher("1,4€ svp")
SINON
    afficher("3,4€ svp")

FIN
"""

age = int(input("Quel age avez vous?"))
toulousain = int(input("Etes vous toulousains?(o=1/n=0)"))

if age < 7 or age >= 65:
    print("gratuit")
elif toulousain == 1 and age < 25:
    print("1,4€ svp")
else:
    print("3,4€ svp")
