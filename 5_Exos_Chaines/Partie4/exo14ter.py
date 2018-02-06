from outils import *


def renverse(chaine):
    """Renvoie une version renversée de chaine."""
    res = ""
    for c in reversed(chaine):
        res += c
    return res


afficher('Entrer une phrase : ')
phrase = lire_chaine()

res = ''
for i in range(0, len(phrase), 5):
    res += renverse(phrase[i:i + 5])

afficher_ligne(res)
