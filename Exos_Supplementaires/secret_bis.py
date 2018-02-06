""" deviner un nombre choisi par l'utilisateur.
    * Ce nombre est compris entre 1 et 100. L'idée est de diminuer l'espace de recherche
    * à chaque itération. Initialement, on commence donc par proposer le milieu (50)
    * puis, en fonction de la réponse, on part à droite ou à gauche.
    * C'est donc une recherche dichotomique
"""

# Programme principal

MAX = 100

print("Pensez à un nombre compris entre 1 et", MAX, "...")

nb_coups = 0
trouve = False
deb, fin = 0, MAX

while not trouve:
    # calcul de la valeur médiane
    milieu = (deb + fin) // 2

    choix = " "
    while choix not in "+-=":
        print("Le nombre secret est", milieu, " ?")
        print("Tapez '-' si mon choix est trop haut")
        print("Tapez '+' si mon choix est trop bas")
        choix = input("Tapez '='pour signaler que j'ai trouvé votre secret... : ")

    nb_coups += 1

    if choix == "+":
        deb = milieu + 1
    elif choix == "-":
        fin = milieu - 1
    else:
        print("Votre secret était donc", milieu)
        print("J'ai trouvé en", nb_coups, "coups")
        trouve = True
