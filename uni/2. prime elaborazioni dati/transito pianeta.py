import matplotlib.pyplot as plt
import numpy as np

dat = np.genfromtxt('transito.txt')
t = dat[:,0]
f = dat[:,1]

fr = f[np.where(f>0.982)]
fb = f[np.where(f<0.958)]
tr = t[np.where(f>0.982)]
tb = t[np.where(f<0.958)]
tn = t[np.where(0.958<f) and np.where(f<0.982)]
fn = f[np.where(0.958<f) and np.where(f<0.982)]

mr = np.sum(fr)/np.size(fr)
mb = np.sum(fb)/np.size(fb)

pt = mr-mb

plt.plot(tr, fr, 'o', mec='black', mew=0.5, color='r', label='out of transit')
plt.plot(tn, fn, 'o', mec='black', mew=0.5, color='black')
plt.xlabel("fase")
plt.ylabel("magnitudo")
plt.xlim(-0.1, 1.0)
plt.ylim(0.8, 1.05)
plt.axhline(y=mr, color='r', label='out of transit')
plt.axhline(y=mb, color='c', label='in transit')
plt.legend(numpoints=1, loc="lower left")

plt.show()
