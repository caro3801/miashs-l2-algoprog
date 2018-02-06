# Exercice 2 : écrire
# un sous-programme qui calcule le minimum de 2 nombres
# un sous-programme qui calcule le maximum de 2 nombres
# un programme qui calcule et affiche le minimum et le maximum de 3 nombres

def min2(x, y):
    return x if x <= y else y
    
def max2(x, y):
    return x if x >= y else y

nb1 = int(input("Entrez un nombre : "))
nb2 = int(input("Entrez un nombre : "))
nb3 = int(input("Entrez un nombre : "))

print("Le plus petit des 3 est {}".format(min2(min2(nb1, nb2), nb3)))
print("Le plus grand des 3 est {}".format(max2(max2(nb1, nb2), nb3)))
