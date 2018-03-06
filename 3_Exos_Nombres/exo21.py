"""déterminer si un entier donné par l'utilisateur est un nombre de Harshad.
Un nombre de Harshad est un entier divisible par la somme de ses chiffres ; exemples : 10, 12, 18, 20."""
nb = input("Donner un nombre : ")
somme=0
for i in range(len(nb)):
    somme+=int(nb[i])
divisible = int(nb) % somme == 0

if divisible :
    print(nb + " est divisible par",somme)
else:
    print(nb + " n'est pas divisible par",somme)