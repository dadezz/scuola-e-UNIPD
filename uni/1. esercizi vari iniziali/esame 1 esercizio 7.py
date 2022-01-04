#Esercizio 7 esame 1
#successione: N0=1, N1=3, N2=2, ..., Nn=1.5N(n+1)+N(n-3) con n>2
#calcolare i primi 14
l = [1, 3, 2]

for i in range (13):
    if i > 2:
        n = 1.5*l[i-1]+l[i-3]
        l.append(n)

print (l)
