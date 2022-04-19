def controllo (z,a):
    for p in range (len(z)):
        if a==z[p]:
            return True

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
                while controllo(z,a):
                    a=int(input("numero non valido, inseriscine un altro"))
                    z[i]=a
                    
    return z

print (cl(z))
