import numpy as np
import matplotlib.pyplot as plt

#massa O
dat=np.genfromtxt('1cm o.txt')

#massa O'
mas=np.genfromtxt('1 cm m.txt')

x=dat[:,0] #lunghezza
y=dat[:,1] #tempi

x1=mas[:,0]
y1=mas[:,1]

plt.plot(x,y, '.r', label="Punti asse O")
plt.plot(x1,y1,'.k', label="Punti asse O'")
plt.plot(x,y,color='orchid', label="Linea congiungente i punti di O")
plt.plot(x1,y1,color='aquamarine', label="Linea congiungente punti di O'")
plt.xlabel("Distanza dal coltello (cm)")
plt.ylabel("Periodo di oscillazione (s)")
plt.legend(loc="upper right")
plt.show()
