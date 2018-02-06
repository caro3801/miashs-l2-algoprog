# 3.1 : demander le nom et le sexe à l'utilisateur et afficher : « cher
# monsieur xx » ou « chère madame xx ».
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
