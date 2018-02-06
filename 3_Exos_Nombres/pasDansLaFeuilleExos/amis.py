import math


def somme_div_propres(n: int) -> int:
    """Calcule la somme des diviseurs propres de n. 
    Version non optimisée (s'arrête à n/2)"""
    res = 1
    for diviseur in range(2, n // 2 + 1):
        if n % diviseur == 0:
            res += diviseur
    return res


def somme_div_propres_opt(n: int) -> int:
    """Calcule la somme des diviseurs propres de n. 
    Version optimisée (s'arrête à sqrt(n))"""
    res = 1
    lim = int(math.sqrt(n))
    for diviseur in range(2, lim):
        if n % diviseur == 0:
            res += diviseur + (n // diviseur)
    # si n est un carré parfait, il faut l'ajouter au résultat
    if n == lim * lim:
        return res + lim
    else:
        return res

# Programme principal : comparez les temps d'exécutions de somme_div_propres et somme_div_propres_opt

sdp = somme_div_propres_opt     # ou sdp = somme_div_propres 
                                #  (et aller se préparer un café...)
if __name__ == '__main__':
    for x in range(3, 100000):
        y = sdp(x)
        if y > x and sdp(y) == x:
            print("({}, {})".format(x, y), end=", ")
    print()
