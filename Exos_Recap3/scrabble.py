"""Le programme tire 7 lettres et les affiche ; le joueur propose un mot et
le programme indique si le mot est bien formé des lettres tirées.
Complément : compter le nombre de points que rapporte un mot."""

from outils import *

# Tirage de 7 lettres aléatoires
liste_lettres = ""
for _ in range(7):
    liste_lettres += chr(aleatoire(ord("a"), ord("z")))

afficher_ligne("Les caractères autorisés sont : ", liste_lettres)

afficher("Entrez un mot : ")
mot = lire_chaine()

# Le mot est correct si chacune de ses lettres est dans liste_lettres
# C'est un while car on s'arrête dès que possible
correct = True
i = 0
while i < len(mot) and correct:
    if mot[i] in liste_lettres:
        correct = True
        # Il faut aussi ôter la lettre de liste_lettres
        j = liste_lettres.index(mot[i])  # indice de la lettre
        liste_lettres = liste_lettres[:j] + liste_lettres[j+1:]
    else:
        correct = False
    i += 1

if correct:
    afficher_ligne(mot, "est correct")
else:
    afficher_ligne(mot, "n'est pas correct")
