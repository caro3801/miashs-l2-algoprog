"""jouer au blackjack avec l'ordinateur"""

import random


def tirage_carte():
    return random.randint(1, 13)


def valeur_carte(carte, qui, montrer=False):
    valeur = carte

    quoi = str(carte)

    if carte == 1:  # cas de l'as
        valeur = 11
        quoi = "As (11)"
    elif (carte == 11):  # valet, dame et roi valent 10
        quoi = "Valet (10)"
        valeur = 10
    elif (carte == 12):
        quoi = "Dame (10)"
        valeur = 10
    elif (carte == 13):
        quoi = "Roi (10)"
        valeur = 10

    if (montrer):
        print(qui, "a pioché :", quoi)
    return valeur


def assurer():
    return bool(input("Voulez vous vous assurer? (1/2 mise) [1 = oui, 0 = non]? "))


def split(carte1, carte2):
    if (carte1 == carte2):
        print()
        return bool(int(input("Voulez vous spliter votre jeu? (double la mise) [1 = oui, 0 = non] ")))
    else:
        return False


def doubler(jeu, current_somme):
    return bool(int(input("Voulez vous doubler ", jeu, " (", current_somme,
                          ")? (double la mise + tirer carte) [1 = oui, 0 = non]")))


def blackjack1(c1, c2):
    return (c1 == 11 and c2 == 10) or (c1 == 10 and c2 == 11)


def resultat(jeu, somme, mise, ordi):
    if somme > ordi and somme <= 21:
        print(jeu, " a gagne")
        resume(jeu, somme, mise)
    elif somme < ordi:
        print("ordi a gagne")
    else:
        print("21 est dépassé c'est perdu!")


def resume(jeu, somme, mise):
    return "[" + jeu + "]" + somme + "rapporte" + mise


def jouer():
    somme_ordi = 0
    somme1_joueur = 0
    somme2_joueur = 0
    mise1_joueur = 20
    mise2_joueur = 0
    assurance = 0
    perdu = False

    # distribution

    # ordi tire 1 carte face visible
    somme_ordi += valeur_carte(tirage_carte(), "ordi", True)
    if (somme_ordi == 11):  # as -> le joueur peut s'assurer contre un blackjack de l'ordi
        if (assurer()):
            assurance = mise1_joueur / 2

    # joueur tire 2 cartes face visible
    carte1 = valeur_carte(tirage_carte(), "joueur", True)
    carte2 = valeur_carte(tirage_carte(), "joueur", True)

    if (blackjack1(carte1, carte2)):
        print("jeu1 gagne")
    else:
        # split?
        if (split(c1, c2)):
            somme1_joueur += carte1
            somme2_joueur += carte2
            mise2_joueur = mise1_joueur  # double la mise
        else:
            somme1_joueur += carte1 + carte2

        croupierEnLice = True
        continuer1 = True
        continuer2 = somme2_joueur != 0
        continuer3 = (somme_ordi < 17 and somme_ordi <= somme1_joueur)
        doubler1Encore = True
        doubler2Encore = True
        while (continuer1 or continuer2 or continuer3):

            if (continuer1):  # jeu1
                doubler1Encore = doubler("jeu1", somme1_joueur)
                if doubler1Encore:
                    mise1_joueur *= 2  # double la mise
                    somme1_joueur += valeur_carte(tirage_carte(), "joueur jeu1", True)  # tire carte face cachee
                    print("jeu1 vaut", somme1_joueur)
                continuer1 = somme1_joueur <= 21 and doubler1Encore
            if (continuer2):  # jeu2
                doubler2Encore = doubler("jeu2", somme2_joueur)
                if doubler2Encore:
                    mise2_joueur *= 2  # double la mise
                    somme2_joueur += valeur_carte(tirage_carte(), "joueur jeu2", True)  # tire carte face cachee
                    print("jeu2 vaut", somme2_joueur)
                continuer2 = somme2_joueur != 0 and somme2_joueur <= 21 and doubler2Encore

            continuer3 = (somme_ordi < 17 and somme_ordi <= somme1_joueur)
            if (continuer3):
                if (somme_ordi <= somme1_joueur):
                    somme_ordi += valeur_carte(tirage_carte(), "ordi", True)
                    print("ordi vaut", somme_ordi)
                    croupierEnLice = (somme_ordi <= 21)

        print(somme_ordi)
        if (not croupierEnLice):
            print("casino perdu")
        else:
            if (somme1_joueur == somme_ordi):
                print("egalite jeu1")
            elif (somme2_joueur == somme_ordi):
                print("egalite jeu2")
            else:
                if (somme1_joueur <= 21 and somme1_joueur > somme_ordi):
                    print("jeu1 gagne")
                else:
                    print("casino gagne, jeu1 perd")

                if somme2_joueur <= 21 and somme2_joueur != 0:
                    if (somme2_joueur > somme_ordi):
                        print("jeu2 gagne")
                    else:
                        print("casino gagne, jeu2 perd")
