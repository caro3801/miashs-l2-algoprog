"""Le but de cet exercice est de montrer qu'il faut d'abord écrire les
fonctions de base qui pourront ensuite servir à écrire dess fonctions plus
complexes, un peu comme du Lego.
On montre aussi comment utiliser assert (premier exemple de tests
unitaires...)"""


def min2(x, y):
    """Renvoie la plus petite des deux valeurs"""
    if x < y:
        return x
    else:
        return y


def min3(x, y, z):
    """Renvoie la plus petite des trois valeurs"""
    # Surtout, on ne récrit pas tout !
    return min2(x, min2(y, z))


def max2(x, y):
    """Renvoie la plus grande des deux valeurs"""
    if x < y:
        return y
    else:
        return x


def max3(x, y, z):
    """Renvoie la plus grande des trois valeurs"""
    # Surtout, on ne récrit pas tout !
    return max2(x, max2(y, z))


# Exemple de programme de test avec des assertions...
if __name__ == '__main__':
    assert min3(12, 42, 3) == 3, "Erreur dans min3"
    assert max3(12, 42, 3) == 42, "Erreur dans max3"
