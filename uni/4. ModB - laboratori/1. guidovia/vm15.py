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


v=[]
v1=[]
v2=[]
v3=[]
v4=[]
for i in range(30,len(x),30):
    vm=((y[i]-y[i-30])/(x[i]-x[i-30]))
    v.append(vm)

for i in range(30,len(x1),30):
    vm1=((y1[i]-y1[i-30])/(x1[i]-x1[i-30]))
    v1.append(vm1)
    
for i in range(30,len(x2),30):
    vm2=((y2[i]-y2[i-30])/(x2[i]-x2[i-30]))
    v2.append(vm2)
    
for i in range(30,len(x3),30):
    vm3=((y3[i]-y3[i-30])/(x3[i]-x3[i-30]))
    v3.append(vm3)
    
for i in range(30,len(x4),30):
    vm4=((y4[i]-y4[i-30])/(x4[i]-x4[i-30]))
    v4.append(vm4)

print(v,v1,v2,v3,v4)


    
    
    
