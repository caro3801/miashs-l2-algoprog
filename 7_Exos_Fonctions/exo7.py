# Exercice 7 : Une balle chute de 400 pixels ; à chaque rebond, la hauteur
# diminue de 10% ; afficher la hauteur du rebond tant qu'il est supérieur à 5
# pixels ; afficher le nombre de rebonds.


def next_rebond(init, attenuation):
    """Calcule la hauteur du rebond suivant, où init est la hauteur du rebond
    initial (en pixels) et attenuation est l'atténuation (en %)
    On arrondit le résultat en entier car c'est un nombre de pixels"""
    return int(init * (1 - attenuation / 100))


hauteur = int(input("Entrez la hauteur initiale du rebond : "))
perte = int(input("Entrez la perte de chaque rebond en pourcentage : "))
seuil = int(input("Entrez le seuil minimal du rebond : "))
nb_rebonds = 0

while hauteur >= seuil:
    print(hauteur, end=" ")
    hauteur = next_rebond(hauteur, perte)
    nb_rebonds += 1

print("\nLa balle a fait", nb_rebonds, "rebonds")
