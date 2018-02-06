from robot import *
init("mon carre")
nb_pas = 200
baisser()
for nb_cotes in range(4):
    avancer(nb_pas)
    droite()

quitter()