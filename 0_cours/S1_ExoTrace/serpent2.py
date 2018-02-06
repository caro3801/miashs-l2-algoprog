from robot import *

init("serpent")
nb_pas = 30
decalage = 10
baisser()

for nb_carre in range(10):
    for nb_cotes in range(2):
        avancer(nb_pas)
        droite()
    nb_pas = nb_pas + decalage
quitter()
