"""Convertir un entier (nombre de secondes) donné par l'utilisateur en heures, minutes, secondes"""

"""
DEBUT
afficher("Nombre de secondes à convertir")
lire(nbsc)

nbh = nbsc // (3600)

nbm = (nbsc - nbh * 3600) // 60

nbs = (nbsc - nbh * 3600 - nbm * 60)

afficher(nbsc,"s équivaut à ",nbh,"H",nbm,"m",nbs,"s")

FIN
"""
nbsc = int(input("Nombre de secondes à convertir : "))

nbh = nbsc // (3600)

nbm = (nbsc - nbh * 3600) // 60

nbs = (nbsc - nbh * 3600 - nbm * 60)

print(nbsc,"s équivaut à ",nbh,"h",nbm,"m",nbs,"s")