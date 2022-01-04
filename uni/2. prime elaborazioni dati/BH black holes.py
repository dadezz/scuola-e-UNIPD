import matplotlib.pyplot as plt
import numpy as np

dat = np.genfromtxt("BH.txt")
m = dat[:,0]
s = dat[:,1]

plt.plot(m,s,'ob',label='misure')  
plt.legend(loc="upper left")  #legenda
plt.xlabel("log(massa)") #scritta nell'asse ascisse
plt.ylabel("sigma") #idem

#n = len(m)
#sumx = np.sum(m)
#sumy = np.sum(s)
#sumx2 = np.sum(m**2)
#sumxy = np.sum(m*s)
#delta = n*sumx2-sumx*sumx

#A = (sumx2*sumy - sumx*sumxy) / (delta)
#B = (n*sumxy - sumx*sumy) / (delta)
#z=A+B*m

#plt.plot(m,z, label='fit')


p=np.polyfit(m,s,1)
x=p[1]+p[0]*m
plt.plot(m,x, "g", label="fitnuovo")
plt.legend()
plt.show()
