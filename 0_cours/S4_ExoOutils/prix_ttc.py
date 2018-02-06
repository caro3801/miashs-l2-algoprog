from outils import *

afficher("Prix hors taxe (HT) ")
prix_ht = lire_nombre()

afficher("Taxe sur la Valeur Ajoutée (TVA) ")
tva = lire_nombre()

prix_ttc = prix_ht * (1 + tva/100)
afficher(prix_ttc)
