def controllo (a,j,i):
    for p in range (j):
        if a==z[p]:
            while a==z[p]:
                a=int(input("numero non valido, inseriscine un altro"))
                z[i]=a
z=[]
def cl(z):
    ris=[]
    for i in range (10):
        a=int(input ("metti sta roba: "))
        z.append(a)
        if a==0:
            break
        for j in range (i):
            if a==z[j]:
                while a==z[j]:
                    a=int(input("numero non valido, inseriscine un altro"))
                    z[i]=a
                    controllo (a,j,i)
    return z

print (cl(z))
