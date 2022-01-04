#Davide Zmbon

a = ["salve",  "ciao", "giorno"]
a += ["beh", "sera", "notte"]

for i in range (len(a)):
    print(a[i])

i = 0
lun = 0

while i < len(a):
    lun += len(a[i])
    i += 1

#print(lun)  non richiesto

a = a[1:]
a[:1] = ["buondì"]

print(a)
