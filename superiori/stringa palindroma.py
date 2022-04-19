#STRINGA PALINDROMA: controlla se la stringa inserita è palindroma o meno
s=input("inserisci la stringa: ")
x=int(len(s)-1)
f=int(x/2)
def spal (s):
    for i in range (0,f):
        z=x-i
        if s[i] != s[x-i]:
            return False
        i=i+1
    return True
if spal (s)== True:
    print ("la stringa è palindroma")
else:
    print("la stringa non è palindroma")
