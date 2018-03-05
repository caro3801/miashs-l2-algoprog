"""calculer les intérêts accumulés chaque année pendant 20 ans par capitalisation
 d'une somme de 100 euros placée au taux fixe de 4,3%"""

"""
DEBUT
annees = 20
sommedep = 100
somme = sommedep
taux = 4.3/100

POUR i allant de 0 à annees non compris FAIRE
    somme +=  somme * taux
FPOUR
afficher("Total : ",somme,". Vous avez accumulé ",somme - sommedep,"d'interets")
FIN
"""

annees = 20
sommedep = 100
somme = sommedep
taux = 4.3/100

for i in range(annees):
    somme +=  somme * taux

print("Total : ",round(somme,2),"€. Vous avez accumulé ",round(somme - sommedep,2),"€ d'interets")