"""afficher une chaine de caractères à l'envers ;
la chaine de caractères est donnée par l'utilisateur."""

"""
DEBUT
afficher("Entrez une chaine à retourner : ")
lire(phrase)
newphrase=""
taille=taille(phrase)-1
POUR i allant de 0 à taille  faire
    newphrase[i]=phrase[taille-i]
FPOUR
afficher_ligne()

FIN
"""

phrase = input('entrer une phrase : ')
taille = len(phrase)
newphrase = ""
for i in range(0, taille):
    newphrase += phrase[taille - 1 - i]

print(newphrase)


# phrase[::-1]
