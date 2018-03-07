from outils import *


def renverse(chaine: str) -> str:
    """Renvoie une version renversée de chaine."""
    res = ""
    for i in range(-1, -len(chaine) - 1, -1):
        res += chaine[i]
    return res


afficher('Entrer une phrase : ')
phrase = lire_chaine()

i = 0
if len(phrase) >= 5:
    j = 5
else:
    j = len(phrase)
fini = False
res = ''

while not fini:
    ''' boucle for avec k inutile '''
    for k in range(i, j + 1):
        segment = renverse(phrase[i:j])
        res = res + segment
        i = j
        if i + 5 <= len(phrase):
            j = i + 5
        else:
            j = len(phrase)
            fini = True

afficher_ligne(res)
