import numpy as np
import matplotlib.pyplot as plt

dat=np.genfromtxt("RV.dat")
v=dat[:,0]
s=dat[:,1]

vgal=v[np.where(v>210)] #velocità della galassia >210
sgal=s[np.where(v>210)]

w=1/(sgal**2)
mpes=np.sum(vgal*w/np.sum(w))#formula media pesata

h=plt.hist(v, bins=70, normed="True")
plt.plot([mpes,mpes],[0,1])

plt.xlabel("velocita radiale")
plt.ylabel("frequenza")

plt.show()

