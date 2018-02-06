# Exo 1-1 : calculer et afficher les 10 premier termes de la table de
# multiplication de 4

# Pour chaque nombre de 1 à 10...
def table_mult_4():
    for i in range(1, 11):
        # On affiche i x 4
        print(i, "x 4 = ", i * 4)


# Exercice 1-2 : calculer et afficher les 10 premier termes de la table de
# multiplication d'un entier donné par l'utilisateur

def table_mult(par):
    for i in range(1, 11):
        # On affiche i x par
        print(i, "x", par, "=", i * par)


# Exercice 1-3: calculer et afficher les termes i à j de la table de
# multiplication d'un entier donné par l'utilisateur, i et j étant donnés par
# l'utilisateur.
# On note qu'en fait, table_mult est un cas particulier de table_mult2 puisque
# il suffit d'appeler table_mult(1, 10, par)
# De même, table_mult_4 est équivalente à table_mult(4)

def table_mult2(deb, fin, par):
    for i in range(deb, fin + 1):
        # On affiche i x par
        print(i, "x", par, "=", i * par)


table_mult(5)
table_mult2(3, 7, 5)
