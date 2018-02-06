from outils import *


def renverse(chaine):
    """Renvoie une version renversée de chaine."""
    res = ""
    for c in reversed(chaine):
        res += c
    return res


afficher('Entrer une phrase : ')
phrase = lire_chaine()

i = 0

fini = False
res = ''
while i <= len(phrase):
    res = res + renverse(phrase[i:i + 5])
    i = i + 5

afficher_ligne(res)
