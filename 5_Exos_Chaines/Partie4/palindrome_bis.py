from outils import *


def renverse(chaine):
    """Renvoie une version renversée de chaine."""
    res = ""
    for i in range(-1, -len(chaine) - 1, -1):
        res += chaine[i]
    return res


afficher('Entrer une phrase : ')
phrase = lire_chaine()

moitie = len(phrase) // 2
gauche = phrase[0:moitie]

if (len(phrase) % 2) == 0:
    droite = phrase[moitie:]
else:
    droite = phrase[moitie + 1:]

if gauche != renverse(droite):
    afficher_ligne("NON. Pas palindrome")
else:
    afficher_ligne("palindrome")
