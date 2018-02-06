"""Codage/décodage d'une chaîne selon le chiffre de César. 
   Voir https://fr.wikipedia.org/wiki/Chiffrement_par_décalage.
   La seule difficulté consiste à tenir compte de la différence min/maj"""

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
