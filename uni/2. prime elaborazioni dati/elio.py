import matplotlib.pyplot as plt
import numpy as np

dati = np.genfromtxt("elio")
m = dati[:,0]
h = dati[:,1]

p = np.polyfit(m,h,3)
z = p[3]+p[2]*m+p[1]*(m**2)+p[0]*(m**3)

plt.plot(m,z, label = "fit")
plt.plot(m,h,"or",label="misure")
plt.xlabel("logM")
plt.ylabel("he")

plt.legend()
plt.show()
