import math     # Pour sqrt...


def somme_div_propres(nb):
    """Renvoie la somme des diviseurs propres de nb.
    Méthode naïve : on s'arrête à nb/2"""
    res = 1     # 1 est toujours dans les diviseurs propres
    for div in range(2, nb // 2 + 1):
        if nb % div == 0:
            res += div
    return res


def somme_div_propres_optim(nb):
    """Renvoie la somme des diviseurs propres de nb.
    Méthode optimisée : on s'arrête à sqrt(nb)"""
    res = 1     # 1 est toujours dans les diviseurs propres
    lim = int(math.sqrt(nb))
    for div in range(2, lim + 1):
        if nb % div == 0:
            res += div + nb // div
    if nb == lim * lim:  # Si nb est un carré parfait
        res -= lim       # il faut ôter sqrt(res)
    return res


def premier(nb):
    """Teste si nb est un nombre premier"""
    # nb est premier si ses seuls diviseurs sont 1 et lui-même
    return somme_div_propres_optim(nb) == 1


def parfait(nb):
    """Teste si nb est un nombre parfait"""
    # nb est parfait s'il est égal à la somme de ses div propres
    return nb == somme_div_propres_optim(nb)
