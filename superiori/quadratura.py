#prima prova di quadratura con ciclo for
z=int(input("inserisci un numero "))
a=0
for n in range(1, 2*z, 2):
      a += n

print ("il quadrato di ",z," e' ",a)
