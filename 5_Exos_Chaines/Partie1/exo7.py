"""
déterminer si un mot est un palindrome ; le mot est donné par l'utilisateur.
"""
"""
DEBUT
afficher("Entrez une chaîne : ")
lire(chaine)

deb = 0
fin = taille(chaine) - 1

TANTQUE deb < fin ET chaine[deb] == chaine[fin]:
    deb += 1
    fin -= 1
FTANQUE

SI deb >= fin ALORS
    afficher_ligne(chaine, "est un palindrome")
SINON
    afficher_ligne(chaine, "n'est pas un palindrome")
FIN
"""

from outils import *

afficher("Entrez une chaîne : ")
chaine = lire_chaine()

deb = 0
fin = len(chaine) - 1

while deb < fin and chaine[deb] == chaine[fin]:
    deb += 1
    fin -= 1

if deb >= fin:
    afficher_ligne(chaine, "est un palindrome")
else:
    afficher_ligne(chaine, "n'est pas un palindrome")
