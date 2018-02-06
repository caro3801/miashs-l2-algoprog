# coding: utf-8
"""
   Un module pour tracer des figures géométriques à l'aide
   d'opérations de dessin primitives.

   Modélise un robot traceur disposant d'un stylet se déplaçant
   sur une feuille de dessin. Ce stylet peut être baissé
   (au contact de la feuille) ou levé (pas de contact avec la feuille).

    - Quel que soit son contact avec la feuille, le stylet avance ou recule selon
     sa direction courante (qui est le nord par défaut).
    - Une commande permet également de le replacer au centre de la feuille.
    - Le stylet peut être orienté dans les 4 directions (nord, sud, est, ouest).
    - Il peut également pivoter vers la droite ou vers la gauche par rapport à
     son orientation courante, ou selon un angle exprimé en degrés (qui est toujours
     considéré comme étant vers la droite de la position courante).
    - La couleur de tracé est noire par défaut, mais elle peut être modifiée, auquel
     cas le tracé restera de la couleur choisie jusqu'au prochain changement de couleur.
"""

import turtle

__robot = None


def init(titre="", largeur=640, hauteur=480):
    """ Initialise l'environnement  (titre et taille de la fenêtre) et place le
    robot au centre, en position baissée, orienté vers le nord, tracé de couleur noire """
    global __robot
    #__robot = turtle.Turtle()
    turtle.setup(largeur, hauteur)
    turtle.Screen()
    turtle.title(titre)
    turtle.mode('logo')
    __robot = turtle.Turtle()


def nord():
    """ Oriente le robot vers le nord """
    __robot.setheading(0)


def sud():
    """ Oriente le robot vers le sud """
    __robot.setheading(180)


def est():
    """ Oriente le robot vers l'est """
    __robot.setheading(90)


def ouest():
    """ Replace le robot vers l'ouest """
    __robot.setheading(270)


def couleur(coul):
    """ Modifie la couleur du stylet. Les couleurs possibles sont :
        blanc, noir, rouge, vert, bleu, jaune, violet. Ces couleurs
        sont des chaînes de caractères : couleur("violet"),
        par exemple."""
    couleurs = {'blanc': 'white', 'rouge': 'red',
                'vert': 'green', 'bleu': 'blue',
                'jaune': 'yellow', 'violet': 'purple'}

    if coul in couleurs:
        __robot.color(couleurs[coul])
    else:
        __robot.color('black')


def avancer(nb_pas=1):
    """ Avance de nb_pas dans la direction courante """
    __robot.forward(nb_pas)


def reculer(nb_pas=1):
    """ Recule de nb_pas dans la direction courante """
    __robot.backward(nb_pas)


def pivoter(nb_degres):
    """ Pivote le robot de nb_degres vers la droite """
    __robot.right(nb_degres)


def droite():
    """ Pivote de 90° vers la droite par rapport à l'orientation courante """
    __robot.right(90)


def gauche():
    """ Pivote de 90° vers la gauche par rapport à l'orientation courante """
    __robot.left(90)


def lever():
    """ Lève le stylet s'il est baissé """
    __robot.up()


def baisser():
    """ Met le stylet au contact de la feuille """
    __robot.down()


def centrer():
    """ Replace le stylet au centre orienté au nord """
    __robot.home()


def cacher():
    """ Cache le curseur de tracé """
    __robot.hideturtle()


def quitter():
    """ Attend que l'utilisateur clique pour fermer la fenêtre """
    turtle.exitonclick()

# Test d'utilisation du module
if __name__ == '__main__':
    import math

    # Initialise l'environnement de tracé avec le robot orienté au nord
    init("Carré, diagonales et médiatrices")

    # Tracé du carré
    for _ in range(4):
        droite()
        avancer(150)

    # Tracé des diagonales (on est dans le coin supérieur geuche, orienté au nord)
    pivoter(135)
    couleur('rouge')
    avancer(150 * math.sqrt(2))

    lever()
    nord()
    avancer(150)
    pivoter(225)
    baisser()
    couleur('violet')
    avancer(150 * math.sqrt(2))

    # Tracé des médianes
    couleur('bleu')
    lever()
    est()
    avancer(75)
    baisser()
    nord()
    avancer(150)
    lever()
    est()
    avancer(75)
    sud()
    avancer(75)
    ouest()
    baisser()
    avancer(150)

    cacher()
    quitter()
