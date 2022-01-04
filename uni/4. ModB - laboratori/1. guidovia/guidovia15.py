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


p=n.polyfit(x,y,2)
z=p[2]+p[1]*x+p[0]*x**2
p1=n.polyfit(x1,y1,2)
z1=p1[2]+p1[1]*x1+p1[0]*x1**2
p2=n.polyfit(x2,y2,2)
z2=p2[2]+p2[1]*x2+p2[0]*x2**2
p3=n.polyfit(x3,y3,2)
z3=p3[2]+p3[1]*x3+p3[0]*x3**2
p4=n.polyfit(x4,y4,2)
z4=p4[2]+p4[1]*x4+p4[0]*x4**2

d=p[1]+2*p[0]*x
d1=p1[1]+2*p1[0]*x1
d2=p2[1]+2*p2[0]*x2
d3=p3[1]+2*p3[0]*x3
d4=p4[1]+2*p4[0]*x4


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


vt=[]
for i in range(15,len(d),30):
    vt.append(d[i])

vt1=[]
for i in range(15,len(d1),30):
    vt1.append(d1[i])
vt2=[]
for i in range(15,len(d2),30):
    vt2.append(d2[i])
vt3=[]
for i in range(15,len(d3),30):
    vt3.append(d3[i])

vt4=[]
for i in range(15,len(d4),30):
    vt4.append(d4[i])

for i in range(len(v)):
    print(v[i],vt[i])
for i in range(len(v1)):
    print(v1[i],vt1[i])
for i in range(len(v2)):
    print(v2[i],vt2[i])
for i in range(len(v3)):
    print(v3[i],vt3[i])
for i in range(len(v4)):
    print(v4[i],vt4[i])

plt.plot(x,z)
plt.plot(x1,z1)
plt.plot(x2,z2)
plt.plot(x3,z3)
plt.plot(x4,z4)

plt.plot(x,d)
plt.plot(x1,d1)
plt.plot(x2,d2)
plt.plot(x3,d3)
plt.plot(x4,d4)

print('g=',2*p[0]/(n.sin(0.00436)))

plt.show()

