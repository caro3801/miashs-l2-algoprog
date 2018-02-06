def rechercher(mot, phrase):
    """Renvoie l'indice du début de mot dans phrase, -1 si phrase ne contient
    pas mot"""
    longueur = len(mot)
    for i in range(len(phrase) - longueur + 2):
        if phrase[i:i + longueur] == mot:
            return i

    return -1


def remplacer(mot, phrase, par):
    """Renvoie une version de phrase avec mot remplacé par par"""
    deb = rechercher(mot, phrase)
    if deb != -1:
        return phrase[:deb] + par + phrase[deb + len(mot):]
    else:
        return phrase


def nb_mots(chaine):
    """Suppose que chaine contient des mots séparés par un seul espace.
       En ce cas, compter les mots consiste à compter les espaces et
        à ajouter 1...
        Remarque : il existe les fonction count() et split(), mais c'est de
        la triche"""
    if chaine == "":  # Ne JAMAIS faire confiance à l'appelant...
        return 0
    res = 1  # La phrase contient forcément un mot
    for car in chaine:
        if car == " ":  # Il y a donc un mot de plus
            res += 1
    return res


def renverser(chaine):
    """Renvoie une version renversée de chaine."""
    res = ""
    for i in range(-1, -len(chaine) - 1, -1):
        res += chaine[i]
    return res


def renverser2(chaine):
    """Renvoie une version renversée de chaine."""
    res = ""
    for car in reversed(chaine):
        res += car
    return res


def renverser3(chaine):
    """Renvoie une version renversée de chaine.
       Utilisation d'une tranche inversée (c'est la meilleure solution)"""
    return chaine[::-1]


def bin_to_dec(chaine):
    """Renvoie l'équivalent décimal de la chaîne de 0 et de 1 fournie en paramètre.
       On suppose que cette chaîne est correcte"""
    accu = 0
    # Algo : on parcours la chaine en multipliant à chaque fois l'accu par 2
    # (méthode de Horner)
    for car in chaine:
        accu = (accu * 2) + int(car)
    return accu


def dec_to_bin(nb):
    """Renvoie l'équivalent binaire du nombre décimal passé en paramètre.
       On suppose que ce nombre est positif ou nul."""
    # Algo : on procède par division successives en gardant les restes et on
    # renvoie la chaine de restes inversée
    if nb == 0:
        return "0"
    res = ""
    while nb > 0:
        res += str(nb % 2)
        nb //= 2
    return res[::-1]


# Tests
if __name__ == '__main__':
    assert rechercher("était", "il était une fois") == 3
    assert rechercher("une", "il était une fois") == 9
    assert rechercher("blabla", "il était une fois") == -1
    assert rechercher("il était une fois dans la ville de Foix",
                      "était") == -1
    assert rechercher("était", "") == -1

    assert remplacer("fois", "il était une fois",
                     "histoire") == "il était une histoire"
    assert remplacer("ville", "La ville rose", "fleur") == "La fleur rose"
    assert remplacer("rouge", "La ville rose", "verte") == "La ville rose"

    assert nb_mots("Il était une fois") == 4
    assert nb_mots("") == 0
    assert nb_mots("bla") == 1

    assert renverser("Il était une fois") == "siof enu tiaté lI"
    assert renverser2("Il était une fois") == "siof enu tiaté lI"
    assert renverser3("Il était une fois") == "siof enu tiaté lI"

    assert bin_to_dec("1001") == 9
    assert bin_to_dec("1000") == 8
    assert bin_to_dec("1111") == 15
    assert bin_to_dec("1001") == 9
    assert bin_to_dec("0000") == 0
    assert bin_to_dec("") == 0

    assert dec_to_bin(14) == "1110"
    assert dec_to_bin(0) == "0"
    assert dec_to_bin(9) == "1001"
    assert dec_to_bin(8) == "1000"
