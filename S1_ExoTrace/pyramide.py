from robot import *
init("pyramide")
nb_pas = 30
decalage = 10
baisser()

for nb_carre in range(10):
    for nb_cotes in range(4):
        avancer(nb_pas)
        droite()
    nb_pas = nb_pas + decalage
    lever()
    gauche()
    avancer(decalage/2)
    sud()
    avancer(decalage/2)
    nord()
    baisser()

quitter()