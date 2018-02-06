# les habitants de Zorglub paient l’impôt selon les règles représentées sur la table de décision suivante :
# (... voir énoncé...)
# Ecrire un programme qui indique à un habitant si il est imposable ou non

# Voir exo 3.1
sexe = "M"
while sexe not in "HF":
    sexe = str.upper(input("Homme (H) ou Femme (F) ? "))

age = 0
while not 0 < age <= 110:
    age = int(input("Entrez votre âge : "))

# Remarque: pb dans l'énoncé pour les hommes... 20 n'est pas pris en compte...
if (sexe == "H" and age < 20) or (sexe == "F" and 18 <= age <= 35):
    print("Vous êtes imposable")
else:
    print("Vous n'êtes pas imposable")
