"""permet à l'utilisateur de donner une série de nombres et qui calcule le pourcentage d'occurrences d'un nombre donné."""
nb_nombres = int(input("combien de nombres?"))
nb_a_compter = int(input("quel nombre compter?"))
cpt = 0

for i in range(nb_nombres):
    curr = int(input("Saisir nombre" + str(i)))
    if nb_a_compter == curr:
        cpt += 1

pour = (cpt * 100) / nb_nombres
print(nb_a_compter, "apparait à ", pour, "%")
