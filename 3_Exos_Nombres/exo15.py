"""Calculer la surface d'un cercle, son diamètre étant donné par l'utilisateur"""
"""
DEBUT
import math
afficher("Donner le diamètre du cercle : ")
lire(diametre)

surface = 2 * math.pi * (diametre/2)**2

afficher("La surface d'un cercle de diamètre ",diametre,"est ",surface)

FIN
"""

import math

diametre = int(input("Donner le diamètre du cercle : "))
surface = 2 * math.pi * (diametre/2)**2
print("La surface d'un cercle de diamètre ",diametre,"est ",surface)