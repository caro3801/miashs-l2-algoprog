"""Codage/décodage d'une chaîne selon le chiffre de César.
   Voir https://fr.wikipedia.org/wiki/Chiffrement_par_décalage.
   La seule difficulté consiste à tenir compte de la différence min/maj"""

"""
DEBUT
fonction shift(car, offset):

    SI car N'EST PAS DANS ascii_letters ALORS
        RETOURNER car
    SI car EST DANS ascii_lowercase ALORS
        base = ord("a")
    SINON
        base = ord("A")
    FSI
    RETOURNER chr((ord(car) - base + offset) % 26 + base)


fonction chiffre(message, offset=13):

    result = ""
    POUR car DANS message:
        result += shift(car, offset)

    RETOURNER result

# Programme principal
afficher("Entrez une phrase : ")
lire(phrase)
afficher("En ROT13, la phrase est", chiffre(phrase))
afficher("Avec un décalage de 5, la phrase est", chiffre(phrase, 5))

FIN
"""

from string import *


def shift(car: str, offset: int) -> str:
    """Renvoie car décalé de offset position dans l'alphabet.
       Prend en compte la différence maj/min"""

    if car not in ascii_letters:
        return car
    if car in ascii_lowercase:
        base = ord("a")
    else:
        base = ord("A")

    return chr((ord(car) - base + offset) % 26 + base)


def chiffre(message: str, offset: int = 13) -> str:
    """Chiffre le message avec le décalage indiqué (13 est le décalage
       utilisé par le ROT13)"""

    result = ""
    for car in message:
        result += shift(car, offset)

    return result

# Programme principal

phrase = input("Entrez une phrase : ")
print("En ROT13, la phrase est", chiffre(phrase))
print("Avec un décalage de 5, la phrase est", chiffre(phrase, 5))