"""
  Un module d'outils pour faciliter l'écriture des premiers programmes
  de L1
  Version 201703002
"""
import random


def aleatoire(deb, fin):
    """ Renvoie un entier aléatoire compris entre deb et fin (exclus)"""
    return random.randint(deb, fin)


def lire_nombre():
    """ Lit et renvoie un nombre saisi au clavier. Le type du résultat dépend de
    la saisie : si elle contient un point, le résultat est float. Sinon,
    il est int. En cas d'erreur, lève l'exception ValueError"""
    nbre = input()
    if '.' in nbre:
        return float(nbre)
    else:
        return int(nbre)


def lire_chaine():
    """ Lit et renvoie une chaîne saisie au clavier. """
    return input()


def afficher(*args):
    """Affiche la liste de paramètes, sans produire de retour à la ligne
    Les paramètres sont automatiquement séparés par un espace"""
    print(*args, end="")


def afficher_ligne(*args):
    """Affiche la liste de paramètes, suivis d'un retour à la ligne
    Les paramètres sont automatiquement séparés par un espace"""
    print(*args)


def convert(car):
    """Renvoie la version minuscule et non accentuée de car"""
    if car in "àÀäÄâÂ":
        return "a"
    elif car in "éÉèÈêÊëË":
        return "e"
    elif car in "ïÏîÎ":
        return "i"
    elif car in "ôÔöÖ":
        return "o"
    elif car in "ùÙûÛüÜ":
        return "u"
    elif car in "Çç":
        return "c"
    else:
        return car.lower()


if __name__ == '__main__':
    # Test de aleatoire
    for _ in range(100):
        afficher(aleatoire(1, 101), " ")
    afficher_ligne("fini...")

    # Test de lire_nombre
    val = lire_nombre()
    afficher_ligne(type(val))

    # Test de lire_chaine
    val = lire_chaine()
    afficher_ligne(val)
