#  Conjecture de Syracuse
# On part d'un entier n auquel on fait subir une transformation :
# si n est pair, on le divise par deux ;
# si n est impair, on le multiplie par 3, et ajoute 1.
# Puis, on recommence sur le résultat. Par exemple, en partant de n=10,
# on  obtient : 10 5 16 8 4 2 1 4 2 1 etc.
# Conjecture : quel que soit l'entier n, on finit par retomber sur 1


def test_conjecture(n):
    while n != 1:
        print(n, end=" ")
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
    print(n)


def syracuse(n):
    cpteur = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        cpteur += 1
    return cpteur


val = int(input("Entrez une valeur pour tester la conjecture : "))
test_conjecture(val)

deb = int(input("Entrez la valeur de début : "))
fin = int(input("Entrez la valeur de fin : "))
max = 0
imax = 0

for i in range(deb, fin + 1):
    syr = syracuse(i)
    if syr > max:
        max = syr
        imax = i

print("C'est", imax, "qui a la plus grande durée de vol : ", max)
