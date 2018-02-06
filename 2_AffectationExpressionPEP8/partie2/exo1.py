"""Conversion Fahrenheit en Celsius"""

from outils import *

afficher("Saisir une température en ° Fahrenheit : ")
fahr = lire_nombre()

celsius = (fahr - 32) / 1.8

afficher_ligne(fahr, "°F = ", round(celsius, 2), "°C")
