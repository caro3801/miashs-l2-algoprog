""" 3.1 : demander le nom et le sexe à l'utilisateur et afficher : « cher
 monsieur xx » ou « chère madame xx »."""

"""
DEBUT
afficher("Entrez votre nom : ")
lire(nom)

sexe = "M"
TANTQUE sexe != "H" ET sexe != "F" FAIRE
    afficher("Homme (H) ou femme (F) ? ")
    lire(sexe)
FTANTQUE
SI sexe == "H" ALORS
    print("Cher monsieur", nom)
SINON
    print("Chère madame", nom)
FSI
FIN
"""

from outils import *

afficher("Entrez votre nom : ")
nom = lire_chaine()

# Boucle pour obtenir une réponse valide. On convertit systématiquement
# en majuscule ce qui a été saisi
sexe = "M"
while sexe != "H" and sexe != "F":
    afficher("Homme (H) ou femme (F) ? ")
    sexe = str.upper(lire_chaine())

if sexe == "H":
    print("Cher monsieur", nom)
else:
    print("Chère madame", nom)
