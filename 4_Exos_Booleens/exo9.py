"""demander les coordonnées d'un rectangle et d'un point ; afficher si le point est dans le rectangle"""

"""
DEBUT
afficher("Donner les coordonnées d'un rectange (haut gauche : x1,y1 ; bas droite : x2,y2)")
afficher("x1:")
lire(x1)
afficher("y1:")
lire(y1)
afficher("x2:")
lire(x2)
afficher("y2:")
lire(y2)
afficher("Donner les coordonnées d'un point P(x3,y3)")
afficher("x3:")
lire(x3)
afficher("y3:")
lire(x3)

SI x1 <= x3 <= x2 ET y1 <= y3 <= y2 ALORS
    afficher("le point est dans le rectangle")
SINON
    afficher("le point n'est pas dans le rectangle")
FSI
FIN
"""

print("Donner les coordonnées d'un rectange (haut gauche : x1,y1 ; bas droite : x2,y2)")
x1 = float(input("x1:"))
y1 = float(input("y1:"))

x2 = float(input("x2:"))
y2 = float(input("y2:"))

print("Donner les coordonnées d'un point P(x3,y3)")

x3 = float(input("x3:"))
y3 = float(input("y3:"))

if x1 <= x3 <= x2 and y1 <= y3 <= y2:
    print("le point est dans le rectangle")
else:
    print("le point n'est pas dans le rectangle")
