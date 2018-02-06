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

