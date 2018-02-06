# afficher le plus grand de 3 entiers donnés par l'utilisateur


# Création d'un sous programme pour renvoyer le max de deux nombres
def max2(x, y):
    """Renvoie le plus grand des nombres x et y : cette fonction existe déjà en Python : elle s'appelle max(x, y)"""
    if x >= y:
        return x
    else:
        return y


# Création d'un sous programme pour renvoyer le max de trois nombres
def max3(x, y, z):
    """"Renvoie le plus grand des nombres x, y et z"""
    return max2(x, max2(y, z))  # Ou : return max(x, max(y, z))


nb1 = int(input("Entrez un nombre : "))
nb2 = int(input("Entrez un nombre : "))
nb3 = int(input("Entrez un nombre : "))

print("Le plus grand des trois est ", max3(nb1, nb2, nb3))
