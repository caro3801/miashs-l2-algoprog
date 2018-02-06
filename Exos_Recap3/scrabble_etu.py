import random
def pioche():
    liste_caractere = "aaaaaaaaabbccdddeeeeeeeeeeeeeeeffgghhiiiiiiiijklllllmmmnnnnnnooooooppqrrrrrrssssssttttttuuuuuuvvwxyz"
    liste_caractere_aleatoire = ""
    for ind in range(7):
        liste_caractere_aleatoire += liste_caractere[random.randint(0, len(liste_caractere)-1)]
    return liste_caractere_aleatoire


def validite(chaine):
    liste_car = chaine
    mot = "$"
    lettres_valides = ""
    ind1 = 0
    while lettres_valides != len(mot) and ind1 < len(mot):
        ind2 = liste_car.find(mot[ind1])
        if ind2 == -1:
            print("Veuillez créer un mot avec les lettres suivante :", chaine)
            mot = input()
            liste_car = chaine
            lettres_valides = ""
            ind1 = 0
        else:
            liste_car = liste_car[:ind2] + "*" + liste_car[ind2+1:]
            lettres_valides += mot[ind1]
            ind1 += 1
    return mot


def score(chaine):
    liste_1p = "eainorstul"
    liste_2p = "dmg"
    liste_3p = "bcp"
    liste_4p = "fhv"
    liste_8p = "jq"
    liste_10p = "kwxyz"
    score = 0
    for car in chaine:
        if liste_1p.find(car):
            score += 1
        elif liste_2p.find(car):
            score += 2
        elif liste_3p.find(car):
            score += 3
        elif liste_4p.find(car):
            score += 4
        elif liste_8p.find(car):
            score += 8
        elif liste_10p.find(car):
            score += 10
    return score


def scrabble():

    liste_caractere_aleatoire = pioche()
    liste_caractere = liste_caractere_aleatoire
    mot_joueur = validite(liste_caractere)
    point = score(mot_joueur)
    print("Vous avez un score de ", point, " avec ce mot.")

scrabble()
