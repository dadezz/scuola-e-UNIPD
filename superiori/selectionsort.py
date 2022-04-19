#SELECTION SORT: tipo di ordinamento 
#senza funzionalità preimpostate (min, find), escluso len

def selectionsort (s):          
    j=0
    for i in range (0,lun-1):
        minimo=s[i]
        for z in range (i, lun):
            if s[z]<minimo:
                minimo=s[z]
        for v in range (i, lun):
            if s[v]==minimo:
                j=v
        if i!=j:
            s=s[:i]+s[j]+s[i+1:j]+s[i]+s[j+1:]
    return s


s=input("inserire stringa ")
stringac=s
lun=len(s)
print("la stringa ",stringac," è stata ordinata col selection sort: ",selectionsort(s))
