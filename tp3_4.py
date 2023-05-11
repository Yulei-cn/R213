'''import math

def calculate_lengths(d1, dn, n):
    lengths = []
    for i in range(1, n+1):
        cn = math.pi * (d1 + dn) * i / 2
        length = cn / math.pi
        lengths.append(length)
    return lengths


d0=int(input("Entrez la diamètre de l'axa en mm : "))
n=int(input("Entrez nombre de tours n : "))
l=9
d1=d0+2*l
dn=d0+2*n*l

lengths = calculate_lengths(d1, dn, n)

print("Calcul de la longueur L pour chaque tour :")
for i, length in enumerate(lengths):
    print(f"Tour {i+1}: {length} mm")'''


import math

d0=int(input("Entrez la diamètre de l'axa en mm : "))
n=int(input("Entrez nombre de tours n : "))
l=9
#d1=d0+2*l
#dn=d0+2*n*l
def d(n):
    return (d0+2*n*l)

print("Calcul de la longueur L pour chaque tour :")
L=0
for i in range(n):
    L=L+math.pi*d(i)
    print("Tour:", i+1, "Dismètre mm :",round(d(i+1),1),"-Longueur enroulée mm:",round(L))


print("Caluer de la longueur formule:")
c0=math.pi*d(0)
cn=math.pi*d(n-1)
L=(c0+cn)*(n+0)/2
print("Longurue mm pour %d"%(n),"tours :",L)
