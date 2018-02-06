from outils import *  # pour aleatoire(), afficher_ligne(), lire_lombre()…

def partie():
    secret = aleatoire(1, 101)  # initialise secret avec un nbre au hasard
    nb_essais = 0  # initialise le nombre d'essais déjà effectués

    afficher("Quel niveau souhaitez vous jouer 0=Facile ")
    niveau = lire_nombre()
    #verification saisie
    while niveau != 0 and niveau != 1 and niveau != 2:
        afficher("Erreur -- Quel niveau souhaitez vous jouer 0=Facile ")
        niveau = lire_nombre()

    if niveau == 0:
        nb_essais_max = 10
    elif niveau == 1:
        nb_essais_max = 5
    elif niveau == 2:
        nb_essais_max = 3



    trouve = False  # on n'a pas encore trouvé…

    while nb_essais < nb_essais_max and not trouve:
        afficher("Entrez une valeur comprise entre 1 et 100 : ")
        nombre = lire_nombre()
        nb_essais = nb_essais + 1  # on a joué un essai de plus
        if nombre > secret:
            afficher_ligne("C'est moins…")
        elif nombre < secret:
            afficher_ligne("C'est plus…")
        else:
            afficher_ligne("Bravo, vous avez trouvé en", nb_essais, "coups")
            trouve = True

    if not trouve:  # c'est parce qu'on a épuisé tous nos essais
        afficher_ligne("Désolé, il fallait trouver", secret)

#programme principal
jouer=0
while jouer==0:
    partie()
    afficher_ligne("Souhaitez vous rejouer [0=Oui]?")
    jouer=lire_nombre()



















