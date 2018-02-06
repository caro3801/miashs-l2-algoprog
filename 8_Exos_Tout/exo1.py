def ask_user():
    """demande au joueur le nom et la distance qui le
    sépare de chacun des 2 aliens et renvoie le nom de celui qui est le
    plus près."""
    nom_alien1 = input("Nom du premier alien : ")
    distance1 = int(input("Distance de cet alien : "))
    nom_alien2 = input("Nom du deuxième alien : ")
    distance2 = int(input("Distance de cet alien : "))
    return nom_alien1 if distance1 < distance2 else nom_alien2


if __name__ == '__main__':
    for _ in range(3):
        print("Élimination de", ask_user())
