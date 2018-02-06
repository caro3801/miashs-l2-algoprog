"""Conversion miles/s en km/s (un mile = 1609 m = 1.609km)"""

from outils import *

afficher("Saisir une vitesse en miles/seconde : ")
mps = lire_nombre()

kms = mps * 1.609

afficher_ligne(mps, "mps = ", round(kms, 2), "km/s")
