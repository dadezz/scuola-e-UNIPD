from random import *
def lancio():
    a = [1, 2, 3, 4, 5, 6]
    b = [1, 2, 3, 4, 5, 6]
    shuffle(a)
    shuffle(b)
    dado1 = choice(a)
    dado2 = choice(b)
    return dado1, dado2

def estrazione():
    lista_usciti = []
    for i in range (5):
        b = randint(1, 90)
        while (b in lista_usciti):
            b = randint(1, 90)
        lista_usciti.append(b)
    return lista_usciti

print (lancio())
print (estrazione())
