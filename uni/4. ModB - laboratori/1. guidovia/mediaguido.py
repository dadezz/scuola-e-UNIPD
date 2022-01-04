import numpy as n
import matplotlib.pyplot as plt


dat=n.genfromtxt('C:/Users/utente/OneDrive/Desktop/Dati tracker 30/Dati 15/video1_15primi.txt')
dat1=n.genfromtxt('C:/Users/utente/OneDrive/Desktop/Dati tracker 30/Dati 15/video2_15primi.txt')
dat2=n.genfromtxt('C:/Users/utente/OneDrive/Desktop/Dati tracker 30/Dati 15/video3_15primi.txt')
dat3=n.genfromtxt('C:/Users/utente/OneDrive/Desktop/Dati tracker 30/Dati 15/video4_15primi.txt')
dat4=n.genfromtxt('C:/Users/utente/OneDrive/Desktop/Dati tracker 30/Dati 15/video5_15primi.txt')

x=dat[:,0]
y=dat[:,1]
x1=dat1[:,0]
y1=dat1[:,1]
x2=dat2[:,0]
y2=dat2[:,1]
x3=dat3[:,0]
y3=dat3[:,1]
x4=dat4[:,0]
y4=dat4[:,1]


m=(y[30]+y1[30]+y2[30]+y3[30]+y4[30])/5
print(m)

m1=(y[60]+y1[60]+y2[60]+y3[60]+y4[60])/5
print(m1)

m2=(y[90]+y1[90]+y2[90]+y3[90]+y4[90])/5
print(m2)

m3=(y[120]+y1[120]+y2[120]+y3[120]+y4[120])/5
print(m3)

m4=(y[150]+y1[150]+y2[150]+y3[150]+y4[150])/5
print(m4)

m5=(y[180]+y1[180]+y2[180]+y3[180]+y4[180])/5
print(m5)

m6=(y[210]+y1[210]+y2[210]+y3[210]+y4[210])/5
print(m6)


#DEVIAZIONE STANDARD
h=n.abs(y[30]-m)
h1=n.abs(y1[30]-m)
h2=n.abs(y2[30]-m)
h3=n.abs(y3[30]-m)
h4=n.abs(y4[30]-m)
sigma3=n.sqrt(((h+h1+h2+h3+h4)**2)/5)
eqm3=sigma3**2
em3=sigma3/n.sqrt(5)

h=n.abs(y[60]-m1)
h1=n.abs(y1[60]-m1)
h2=n.abs(y2[60]-m1)
h3=n.abs(y3[60]-m1)
h4=n.abs(y4[60]-m1)
sigma6=n.sqrt(((h+h1+h2+h3+h4)**2)/5)
eqm6=sigma6**2
em6=sigma6/n.sqrt(5)

h=n.abs(y[90]-m2)
h1=n.abs(y1[90]-m2)
h2=n.abs(y2[90]-m2)
h3=n.abs(y3[90]-m2)
h4=n.abs(y4[90]-m2)
sigma9=n.sqrt(((h+h1+h2+h3+h4)**2)/5)
eqm9=sigma9**2
em9=sigma9/n.sqrt(5)

h=n.abs(y[120]-m3)
h1=n.abs(y1[120]-m3)
h2=n.abs(y2[120]-m3)
h3=n.abs(y3[120]-m3)
h4=n.abs(y4[120]-m3)
sigma12=n.sqrt(((h+h1+h2+h3+h4)**2)/5)
eqm12=sigma12**2
em12=sigma12/n.sqrt(5)

h=n.abs(y[150]-m4)
h1=n.abs(y1[150]-m4)
h2=n.abs(y2[150]-m4)
h3=n.abs(y3[150]-m4)
h4=n.abs(y4[150]-m4)
sigma15=n.sqrt(((h+h1+h2+h3+h4)**2)/5)
eqm15=sigma15**2
em15=sigma15/n.sqrt(5)

h=n.abs(y[180]-m5)
h1=n.abs(y1[180]-m5)
h2=n.abs(y2[180]-m5)
h3=n.abs(y3[180]-m5)
h4=n.abs(y4[180]-m5)
sigma18=n.sqrt(((h+h1+h2+h3+h4)**2)/5)
eqm18=sigma18**2
em18=sigma18/n.sqrt(5)

h=n.abs(y[210]-m6)
h1=n.abs(y1[210]-m6)
h2=n.abs(y2[210]-m6)
h3=n.abs(y3[210]-m6)
h4=n.abs(y4[210]-m6)
sigma21=n.sqrt(((h+h1+h2+h3+h4)**2)/5)
eqm21=sigma21**2
em21=sigma21/n.sqrt(5)




print(sigma3, eqm3, em3, sigma6, eqm6, em6, sigma9, eqm9, em9, sigma12, eqm12, em12, sigma15, eqm15, em15,  sigma18, eqm18, em18,  sigma21, eqm21, em21)














