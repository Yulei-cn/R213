print("Calcul du capital acquis et de ses intérêts payés lorsque les intérêts sont calculés une fois par an.")
#s=int(input("Entrez l'investissement de départ : "))
#m=int(input("Entrez le montant du paiement mensuel : "))
#r=float(input("Saisissez le taux annuel en % : "))
#t=int(input("Entrez le nombre d'années : "))
s = 300
m = 45
r = 0.023
t = 8
n = 1
FM = 0.00
for j in range(t):
    FM = m * (((1 + r/n)**(n*t) - 1) / (r/n))
print("€", round(FM, 2))
