import numpy as np
import matplotlib.pyplot as plt

s = np.genfromtxt('RV.dat')
v = s[:,0]
err = s[:,1]

vs = v[np.where(v>210)]
es = err[np.where(v>210)]

mp = np.sum(vs*es)/np.sum(es)
AVm = np.average(vs, None, es)

if mp == AVm:
    print (True)
else:
    print (False)

w=1/(es**2)
er = np.sqrt(1/np.sum(w))
print (er)

plt.hist(v, bins=100, normed=True, color="green", label="misure")
plt.plot([mp,mp], [0,er-0.2], color="orange", label="average")
plt.legend(numpoints=1, loc="upper left")
plt.xlabel("Radial velocity")
plt.ylabel("Freq. of stars")
plt.xlim(175, 220)
plt.show()
