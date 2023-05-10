print("Crédit")
s=int(input("MONTANT DU CRÉDIT : "))
t=float(input("TAUX: "))
n=int(input("DURÉE DE REMBOURSEMENT ANNE: "))

#tm=t/12/100
tm=(1+t/100)**(1/12)-1
a=(1+tm)**(12*n)
m = s * (tm * a) / (a - 1)


print("Mois mensualité	Interêts Capital amorti	  -Reste dû  intérets remboursés")
ir=0
for j in range(n*12):
    i=tm*s
    cr=m-i
    crd=s-cr
    ir=i+ir
    print(" ",j+1,"  - ",round(m,1), " - ",round(i,1), "   - ",round(cr,1), "    - ",round(crd,1), " - ",round(ir,2))
    s=crd


