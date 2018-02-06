import sys


def input_serie():
    """Saisie une série de température sous la forme d'une chaîne de valeurs
    séparées par des espaces"""
    serie = input("Entrez une suite de valeurs séparées par des espaces :")
    return serie


def plus_proche_zero(serie):
    """Renvoie le min et le max d'une série"""
    res = sys.maxsize
    for temp in serie.split():
        temp = abs(int(temp))
        if temp < res:
            res = temp
    return res


if __name__ == '__main__':
    temps = input_serie()
    print("La température la plus proche de zéro est", plus_proche_zero(temps))
