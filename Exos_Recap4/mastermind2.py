"""Jeu du mastermind. Pour simplifier :
    - chaque couleur est représentée par une lettre majuscule
    - l'utilisateur saisit correctement sa tentative
    Les améliorations sont laissées en exercice
    Pourrait faire l'objet d'un mini-projet ?
"""


from outils import aleatoire


# Constantes globale (pour simplifier l'écriture...)
# 8 couleurs possibles : Rouge, Jaune, Vert, Bleu, Orange, Marron, Noir, Gris
COULEURS = "RJVBOMNG"
MAX_COUPS = 10


def cree_combinaison_secrete():
    """Crée une combinaison de 4 couleurs prises parmi RJVBOMNG
       Une couleur ne peut être choisie qu'une seule fois"""
    combi = ""
    deja_joue = ""          # Contient les couleurs déjà tirées au sort
    while len(combi) < 4:   # Il faut avoir choisi 5 couleurs...
        coul = COULEURS[aleatoire(0, 7)]
        if coul not in deja_joue:
            deja_joue += coul
            combi += coul
    return combi


def traite_combinaison(tentative, secret):
    """Renvoie le nbre de couleurs bien placées et mal placées dans la
    tentative du joueur"""
    nb_bien_placees, nb_mal_placees = 0, 0
    # Recherche et marque les bien placés : comme on doit modifier tentative et
    # secret, qui sont immutables, on est obligés de passer par des listes (qui
    # sont modifiables...)
    # Une autre solution serait de passer par des 2 fois 5 variables, mais
    # c'est trop artificiel
    copie_secret = list(secret)
    copie_tentative = list(tentative)

    for i in range(len(secret)):
        if secret[i] == tentative[i]:     # Bien placé, donc on marque
            copie_secret[i] = "X"         # à la fois dans secret
            copie_tentative[i] = "Y"      # et dans tentative
            nb_bien_placees += 1
    # recherche des mal placés qui restent dans la tentative
    for couleur in copie_tentative:
        if couleur in copie_secret:
            copie_secret[copie_secret.index(couleur)] = "X"
            nb_mal_placees += 1
    return nb_bien_placees, nb_mal_placees


def affiche_resultat(combi, nb_bien_placees, nb_mal_placees):
    res = "| " + combi + " | "
    aux = "X" * nb_bien_placees + "x" * nb_mal_placees
    res = res + aux.ljust(4, '.') + " |"
    print(res)


if __name__ == '__main__':
    encore = "o"
    while encore.upper() == "O":
        combi_secrete = cree_combinaison_secrete()
        print("secret :", combi_secrete)
        bien_places = 0
        nb_essais = 1
        while bien_places != 4 and nb_essais < MAX_COUPS:
            essai = input("Essai " + str(nb_essais) + " (RJVBOMNG) : ")
            bien_places, mal_places = traite_combinaison(essai, combi_secrete)
            nb_essais += 1
            affiche_resultat(essai, bien_places, mal_places)
        # Pourquoi est-on sorti ?
        if nb_essais == MAX_COUPS:
            print("Il fallait trouver", combi_secrete)
        encore = input("Voulez-vous rejouer (o/n) ? ")
