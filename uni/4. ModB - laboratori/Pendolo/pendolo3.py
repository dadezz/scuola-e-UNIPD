import numpy as n
import matplotlib.pyplot as plt

dat=n.genfromtxt('Ultimo O primo.txt')
x=dat[:,0]
y=dat[:,1]

dat1=n.genfromtxt('Ultimo O.txt')
x1=dat1[:,0]
y1=dat1[:,1]

p=n.polyfit(x,y,1)  #retta 1 usando polyfit
z=p[1]+p[0]*x
p1=n.polyfit(x1,y1,1) #retta 2 usando polyfit
z1=p1[1]+p1[0]*x1
h=(p[1]-p1[1])/(p1[0]-p[0]) #retta verticale all'intersezione
print(h)


############################ RETTA 1 (x,y) ########################
sumx = n.sum(x)     #Calcolo dei coefficienti A, B
sumy = n.sum(y)
sumx2 = sumx**2
sumxy = sumx*sumy
N = len(x)
delta = N*sumx2-sumx**2
A = (sumx2*sumy-sumx*sumxy)/delta
B = (N*sumxy-sumx*sumy)/delta
somme = []      #calcolo errori dei coefficienti
for i in range(N):
    so = (y[i]-A-B*x[i])**2
    somme.append(so)
sommatoria = n.sum(somme)
sigmay = n.sqrt((1/(N-2))*sommatoria)
sigmab = sigmay*n.sqrt(N/delta) #errore sul coefficiente b
sigmaa = sigmay*n.sqrt(sumx2/delta) #errore sul coefficiente a
############################ RETTA 2 (x1,y1) ########################
sumx1 = n.sum(x1)     #Calcolo dei coefficienti A, B
sumy1 = n.sum(y1)
sumx12 = sumx1**2
sumx1y1 = sumx1*sumy1
N1 = len(x1)
delta1 = N1*sumx12-sumx1**2
A1 = (sumx12*sumy1-sumx1*sumx1y1)/delta1
B1 = (N1*sumx1y1-sumx1*sumy1)/delta1
somme1 = []      #calcolo errori dei coefficienti
for i in range(N1):
    so1 = (y1[i]-A1-B1*x1[i])**2
    somme1.append(so1)
sommatoria1 = n.sum(somme1)
sigmay1 = n.sqrt((1/(N1-2))*sommatoria1)
sigmab1 = sigmay1*n.sqrt(N1/delta1) #errore sul coefficiente b
sigmaa1 = sigmay1*n.sqrt(sumx12/delta1) #errore sul coefficiente a
#####################################################################

print("B retta1 (orchid): ",p[0])
print("A retta1 (orchid): ",p[1])
print("B retta2 (aquamarine): ",p1[0])
print("A retta2 (aquamarine): ",p1[1])
print("sigma b retta1 (orchid): ",sigmab)
print("sigma a retta1 (orchid): ",sigmaa)
print("sigma b retta2 (aquamarine): ",sigmab1)
print("sigma a retta2 (aquamarine): ",sigmaa1)


plt.plot(x,y,'o',color='orchid', label="Punti asse O'")
plt.plot(x1,y1,'o',color='aquamarine', label="Punti asse O")
plt.plot(x,z,color='orchid', label="Retta interpolante punti di O'")
plt.plot(x1,z1,color='aquamarine', label="Retta interpolante punti di O")
plt.axvline(h,color='yellowgreen', label="Punto di intersezione tra le rette")
plt.xlabel("Distanza dal coltello (cm)")
plt.ylabel("Periodo di oscillazione (s)")
plt.legend(loc="upper right")
plt.show()

