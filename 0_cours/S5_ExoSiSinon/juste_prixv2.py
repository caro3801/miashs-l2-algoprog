from outils import *  # pour aleatoire(), afficher_ligne(), lire_lombre()…

secret = aleatoire(1, 101)  # initialise secret avec un nbre au hasard
nb_essais = 0  # initialise le nombre d'essais déjà effectués
afficher("Quel niveau souhaitez vous ? 0=facile, 1= moyen, 2= difficile")
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












