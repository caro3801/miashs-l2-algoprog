"""permet de déterminer si 2 nombres donnés par l'utilisateur sont amis."""
sommeN = sommeM = 0
print("voyons si deux nombres sont amis...")
n = int(input("Nombre N : "))
m = int(input("Nombre M : "))

for i in range(1,min(n,m)):
    if (n % i) == 0 :
        sommeN += i
    if (m % i) == 0 :
        sommeM += i
if sommeN == m and sommeM == n :
    print(n, "et", m, "sont amis.")
else:
    print(n, "et", m, "ne sont pas amis. sommeN:",sommeN,",sommeM",sommeM)
