import matplotlib.pyplot as plt
import numpy as np

dati = np.genfromtxt("hubble")
d = dati[:,0]
v = dati[:,1]
plt.plot(d,v, "or", label = "velocità")
plt.legend()
plt.xlabel("mpc")
plt.ylabel("km/s")
#n = len(d)
#sumx = np.sum(d)
#sumy = np.sum(v)
#sumx2 = np.sum(d**2)
#sumxy = np.sum(d*v)
#delta = n*sumx2-sumx*sumx

#A = (sumx2*sumy - sumx*sumxy) / (delta)
#B = (n*sumxy - sumx*sumy) / (delta)
#z=A+B*d

#plt.plot(d,z, label="reg", color="blue")

p=np.polyfit(d,v,1)
x=p[1]+p[0]*d
plt.plot(d,x, "g", label="fitnuovo")
plt.legend()
plt.show()
