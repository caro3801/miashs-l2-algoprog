""" Teste si un entier saisi au clavier est un nombre palindrome """

from outils import *

afficher("Entrez un nombre entier :  ")
nbre = lire_nombre()

nbre = int(nbre)   # Au cas où on aurait saisi un flottant

# Pour savoir si nbre est un palindrome, on commence par le convertir en
# chaîne de caractères
nbre = str(nbre)

# On applique l'algo classique
deb = 0
fin = len(nbre) - 1
palin = True
while deb < fin and palin:
    if nbre[deb] != nbre[fin]:
        palin = False
    else:
        deb += 1
        fin -= 1

if palin:
    afficher_ligne(nbre, "est un palindrome")
else:
    afficher_ligne(nbre, "n'est pas un palindrome")
