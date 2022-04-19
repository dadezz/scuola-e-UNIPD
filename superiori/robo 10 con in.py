z=[]
def cl(z):
    ris=[]
    for i in range (10):
        a=int(input ("metti sta roba: "))
        z.append(a)
        if a==0:
            break
        for j in range (i):
            while a in z:
                a=int(input("numero non valido, inseriscine un altro"))
                z[i]=a
    return z

print (cl(z))
