#Davide Zambon

succ = [7, 4]
for i in range (13):
    if i > 1:
        N = succ[i-2] - 1/(succ[i-1])
        succ.append(N)

print("i primi 13 numeri sono: ", succ)

#se non vuole che venga stampata una lista basta fare un ciclo for
#e stampare uno alla volta tutti i valori, non è specificato.

somma = 0

for i in range (11):
    somma += succ[i]

print("la somma dei primi 11 elementi vale: ", somma)
