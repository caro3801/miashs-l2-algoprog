# calculer l'obtention du L1 par un étudiant, à partir de sa moyenne au S1 et au S2 ;
# si l'étudiant n'a pas obtenu son L1, afficher s'il a obtenu le S1 ou le S2.

moyenne_S1 = float(input("Moyenne obtenue au S1 : "))
moyenne_S2 = float(input("Moyenne obtenue au S2 : "))

# Un étudiant obtient le L1 s'il a au moins 10 de moyenne au S1 ET au S2
if moyenne_S1 >= 10 and moyenne_S2 >= 10:
    print("L1 validé")
elif moyenne_S1 >= 10 and moyenne_S2 < 10:
    print("S1 obtenu")
elif moyenne_S1 < 10 and moyenne_S2 >= 10:
    print("S2 obtenu")
