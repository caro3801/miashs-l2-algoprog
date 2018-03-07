""" The "Fizz-Buzz test" is an interview question designed to help filter
out the 99.5% of programming job candidates who can't seem to program their
way out of a wet paper bag. The text of the programming assignment is as
follows:

 "Write a program that prints the numbers from 1 to 100. But for multiples
 of three print  “Fizz” instead of the number and for the multiples of five
 print “Buzz”. For numbers which are multiples of both three and five print
 “FizzBuzz”."
"""
"""
DEBUT
POUR nb allant de 1 à 101 non compris FAIRE
    SI nb % 3 == 0 ET nb % 5 == 0 ALORS
        afficher("FizzBuzz ")
    SINON SI nb % 3 == 0 ALORS
        afficher("Fizz ")
    SINON SI nb % 5 == 0 ALORS
        afficher("Buzz ")
    SINON
        afficher(nb, " ")
    FSI
FPOUR
FIN
"""

from outils import *

for nb in range(1, 101):
    if nb % 3 == 0 and nb % 5 == 0:
        afficher("FizzBuzz ")
    elif nb % 3 == 0:
        afficher("Fizz ")
    elif nb % 5 == 0:
        afficher("Buzz ")
    else:
        afficher(nb, " ")
afficher_ligne()
