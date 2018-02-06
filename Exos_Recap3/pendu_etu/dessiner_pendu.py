from robot import *
from outils import *
'''
Auteur: Caroline Desprat
Contenu: Jeu du Pendu avec dessin du pendu 
Note: Script de dessin inspiré du code de l'étudiant Baptiste Charazac
'''
def etape0():
    init()
def etape1() :
    baisser()
    ouest()
    avancer(100)
    est()
    avancer(50)
    
def etape2() :
    nord()
    avancer(200)
    
def etape3() :
    est()
    avancer(100)
    
def etape4() :
    sud()
    avancer(50)

    
def etape5() :
    est() 
    avancer(7)
    sud()
    avancer(14)
    ouest()
    avancer(14)
    nord()
    avancer(14)
    est()
    avancer(7)
    lever()
    sud()
    avancer(14)
    
def etape6() :
    baisser()
    ouest()
    avancer(50)
    est()
    avancer(100)
    ouest()
    avancer(50)
    sud()
    avancer(75)
    pivoter(20)
    avancer(50)
    pivoter(180)
    avancer(50)
    pivoter(140)
    avancer(50)
        
def pendu(num_essai):
    if num_essai == 6 :
        etape0()
    if num_essai == 5 :
        etape1()
    elif num_essai == 4 :
        etape2()
    elif num_essai == 3 :
        etape3()
    elif num_essai == 2:
        etape4()
    elif num_essai == 1 :
        etape5()
    elif num_essai == 0 :
        etape6()



