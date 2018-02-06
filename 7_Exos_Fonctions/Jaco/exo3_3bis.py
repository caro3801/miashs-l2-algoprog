# Exercice 3 : Déterminer si un entier donné par l'utilisateur est divisible 
# par 5.

# nb est divisible par div si le reste de nb/div = 0
def divisible_par(nb, div):
    return False if div == 0 else nb % div == 0
    

nb1 = int(input("Entrez un nombre : "))
nb2 = int(input("Entrez un nombre : "))

if divisible_par(nb1, nb2):
    print(nb1, "est divisible par", nb2)
else:
    print(nb1, "n'est pas divisible par", nb2)  

