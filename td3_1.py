print("Calcul du capital acquis et de ses intérêts payés lorsque les intérêts sont calculés une fois par an.")
#s=int(input("Entrez l'investissement de départ : "))
#m=int(input("Entrez le montant du paiement mensuel : "))
#r=float(input("Saisissez le taux annuel en % : "))
#t=int(input("Entrez le nombre d'années : "))
c0 = 300
m = 45
t = 2.3
n = 8

def c(n):
    if n == 0:
        return c0
    else:
        return ((c(n - 1) + 12 * m) * (1 + t / 100))

print("La capital est", round(c(n), 2), "€")
print("Les intérêts gagnés à", t, "% sont de", round(c(n) - n * m * 12 - c0, 2), "€")
print("Sans intérêts, le total serait de", round(n * m * 12 + c0, 2), "€")
