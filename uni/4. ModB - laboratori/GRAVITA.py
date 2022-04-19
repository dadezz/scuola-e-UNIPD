import numpy as n
import matplotlib.pyplot as plt

dat = n.genfromtxt("Finale.txt")
y = dat[:,1]


media = n.sum(y)/len(y) #media periodi
g=(4*(n.pi)**2*(0.9941/(media)**2)) #calcolo g
erroreg = g*n.sqrt((0.02/94.41)**2+4*(0.001/2.00088)**2)    #calcolo errore 

indice = ["calcolato", "padova"]    #creo array per il plot
valori = [g, 9.806]
errori = [erroreg, 0.001]

plt.errorbar(indice, valori, yerr=errori, fmt='.r', label="Misure di g con relativa barra di errore") #plot con barre di errore
plt.ylabel("g [m/s^2]")
plt.legend()
plt.show()
print(erroreg)
print(g)


#9.80352934308 



