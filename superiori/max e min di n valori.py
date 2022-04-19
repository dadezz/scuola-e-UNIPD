#trovare il massimo e il minimo di n valori inseriti dall'utente
n=int(input("inserire il numero di valori tra cui si vuole trovare il massimo e il minimo: "))
num=int(input("inserire il primo valore: "))
massimo=num
minimo=num
for i in range (1, n):
    num=int(input("inserire il prossimo valore: "))
    if num<minimo:
        minimo=num
    if num>massimo:
        massimo=num
print("il minimo tra i numeri digitati e': " + str(minimo) + "\nil massimo tra i numeri digitati e': " + str(massimo))
