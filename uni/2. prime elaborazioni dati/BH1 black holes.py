import matplotlib.pyplot as plt
import numpy as np
dat = np.genfromtxt('BH1.txt')
logm = dat[:,0]
sig = dat[:,1]
err = dat[:,2]

plt.errorbar(logm, sig, yerr=err, fmt='.r', label='misure')
plt.xlabel('log(massa)')
plt.ylabel('dispersione velocita')
plt.ylim(1, 11)

we = 1/(err*err)
p=np.polyfit(logm, sig, 1, w=we)
z=p[1]+p[0]*logm
plt.plot(logm, z, 'green', label="fit")
plt.legend()
plt.show()
