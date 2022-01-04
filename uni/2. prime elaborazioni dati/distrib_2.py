############ RELAZIA DE RACANELLI ##########
## COSO PER FARE GLI ISTOGRAMMI
import matplotlib.pyplot as plt
import numpy as np

dati = np.genfromtxt('distrib_2.txt')
plt.hist(dati, 25, color="#f400a1", alpha=0.8)
plt.grid(axis="y", alpha=2, color="grey")
plt.xlabel("Misure (cm)")
plt.ylabel("Frequenze")


plt.show()
