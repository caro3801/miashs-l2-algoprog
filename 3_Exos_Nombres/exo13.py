"""calculer la suite de Fibonacci"""

"""
V1 calculer les 15 premiers termes de la suite

nb_termes = 15
somme = 0
POUR i allant de 0 à nb_termes non compris FAIRE
    somme+=i
FPOUR
afficher("somme des ",nb_termes,"premiers termes : ",somme )
"""
def Fibo1():
    nb_termes = 15
    somme = 0
    for i in range(1,nb_termes+1):
        somme+=i

    print("somme des ",nb_termes,"premiers termes : ",somme )


Fibo1()

"""
V2 calculer la suite jusqu'au premier terme supérieur à 100

limite = 100
i = 0
somme = 0
TANTQUE  i <= limite+1 FAIRE
    somme+=i
    i+=1
FTANTQUE
afficher("somme jusqu'au premier terme supérieur à ",limite,": ",somme )
"""
def Fibo2():

    limite = 100
    i = 1
    somme = 0
    while  i <= limite+1:
        somme+=i
        i+=1

    print("somme jusqu'au premier terme supérieur à ",limite,": ",somme )


Fibo2()