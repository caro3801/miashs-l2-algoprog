""" The "Fizz-Buzz test" is an interview question designed to help filter
out the 99.5% of programming job candidates who can't seem to program their
way out of a wet paper bag. The text of the programming assignment is as
follows:

 "Write a program that prints the numbers from 1 to 100. But for multiples
 of three print  “Fizz” instead of the number and for the multiples of five
 print “Buzz”. For numbers which are multiples of both three and five print
 “FizzBuzz”."
"""

# Version "tordue"

from outils import *
for nb in range(1, 101):
    res = ""
    if nb % 3 == 0:
        res += "Fizz"
    if nb % 5 == 0:
        res += "Buzz"
    if res == "":
        afficher(nb, " ")
    else:
        afficher(res, " ")

afficher_ligne()