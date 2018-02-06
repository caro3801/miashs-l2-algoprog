"""Le pendu est un jeu consistant à trouver un mot en devinant quelles sont les
lettres qui le composent. Il se joue traditionnellement à deux, le joueur 1
choisit un mot, le joueur 2 propose une lettre. le programme indique si la
lettre est présente et combien de fois. Il affiche également, au fur et à
mesure le mot avec les lettres trouvées (celles restant à deviner sont
représentées par un ‘*’) et le nombre de lettres restant.

Le nombre d'essais est limité à 6. Chaque fois que le joueur 2 propose une
lettre n’appartenant pas au mot à deviner, il perd 1 crédit; le jeu est bloqué
dès que le joueur 2 a perdu 6 crédits."""

from outils import *

a_deviner = input("Joueur 1 : choissez un mot (sans le montrer à Joueur 2) : ")
print("\n" * 20)
nb_credits = 6
chaine_trouvee = "_" * len(a_deviner)
trouve = False

while nb_credits > 0 and not trouve:
    print(chaine_trouvee)
    # Si on a trouvé le mot, la chaine ne contient plus de _
    trouve = chaine_trouvee.count("_") == 0

    if not trouve:
        # On ne garde que le premier caractère
        lettre = input("Joueur 2 : choisissez une lettre : ")[0]
        if lettre in a_deviner:
            cpt = 0
            for i in range(len(a_deviner)):
                if a_deviner[i] == lettre:
                    cpt += 1
                    chaine_trouvee = modif_chaine(chaine_trouvee, i, lettre)
            print(lettre, "est présente", cpt, "fois dans le mot")
        else:
            nb_credits -= 1
            print("Le mot ne contient pas", lettre)

if not trouve:
    print("Il fallait trouver le mot '", a_deviner, "'")
