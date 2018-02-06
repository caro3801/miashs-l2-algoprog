def codage(mess):
    res = ""
    i = 0
    while i < len(mess):
        if mess[i] == "0":
            res += "00 0"
            current = "0"
        else:
            res += "0 0"
            current = "1"
        i = i + 1
        while i < len(mess) and mess[i] == current:
            res += "0"
            i = i + 1
        res += " "
    return res


if __name__ == '__main__':
    message = ""
    while len(message) < 1:
        message = input("Entrez un message : ")
    reponse = codage(message)
    print("le message encodé est", reponse)
