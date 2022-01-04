########   RANDOM   ###########
import random as r
a = 1
b = 20
s=[1, 2, 3, 4, 5, 6, 7,8, 9]

n = r.randint (a, b) #n casuale intero tra a e b (compresi)
r.shuffle(s) #mescola la sequenza s, non richiede assegnazione
c = r.choice(s) #prende un numero a caso dalla sequenza s
print (n)
print (s)
print (c)
