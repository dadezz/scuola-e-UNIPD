#Davide Zambon#

import matplotlib.pyplot as plt
import numpy as np

dat = np.genfromtxt("NGC2808.dat")
y = dat[:,0]
N = dat[:,1]
n = dat[:,2]
Nestreme = N[np.where(n == 2)]
yestreme = y[np.where(n == 2)]
Nnorm = N[np.where(n == 1)]
ynorm = y[np.where(n == 1)]

ymedioestremo = np.average(yestreme) ## Punto III

#print("la media vale: ", ymedioestremo) se volessi stamparlo (non richiesto)

Nmedionorm = np.average(Nnorm)
Nmedioestremo = np.average(Nestreme)
diff_abb = Nmedionorm - Nmedioestremo ## Punto IV

plt.plot(N, y, label="grafico y in funzione di N") ##Punto I
plt.xlabel("N/Fe")
plt.ylabel("Y")
plt.plot(Nestreme, yestreme,  "or", label="estremi") ##Punto II

p = np.polyfit(Nestreme, yestreme, 1)
z = p[0]+p[1]*Nestreme

plt.plot(z, yestreme, color="yellow", label="fit") ##Punto V

p2 = np.polyfit(N, y, 2)
z2 = p2[2]+p2[1]*N+p2[0]*N**2

plt.plot(z2, y, color="green", label="fit tutto") ##Punto V

plt.legend()
plt.show()

