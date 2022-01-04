import numpy as n
import matplotlib.pyplot as plt

#Importo i file
dat = n.genfromtxt('15/video1_15primi.txt')
dat1 = n.genfromtxt('15/video2_15primi.txt')
dat2 = n.genfromtxt('15/video3_15primi.txt')
dat3 = n.genfromtxt('15/video4_15primi.txt')
dat4 = n.genfromtxt('15/video5_15primi.txt')

#Estraggo i dati
x = dat[:,0]  #time
y = dat[:,1]  #position
x1 = dat1[:,0]
y1 = dat1[:,1]
x2 = dat2[:,0]
y2 = dat2[:,1]
x3 = dat3[:,0]
y3 = dat3[:,1]
x4 = dat4[:,0]
y4 = dat4[:,1]

#Eguaglio le lunghezze (la più corta tra le 5)
x = x[:220] #220 è il più breve tra QUESTI file, va cambiato per ogni angolo
y = y[:220]
x1 = x1[:220]
y1 = y1[:220]
x2 = x2[:220]
y2 = y2[:220]
x3 = x3[:220]
y3 = y3[:220]
x4 = x4[:220]
y4 = y4[:220]

#Calcolo la media dello spostamento per ogni fotogramma dei 5 video
medie = []
for i in range (len(y)):
    media = (y[i]+y1[i]+y2[i]+y3[i]+y4[i])/5
    medie.append(media)
#Ora "Medie" è un array lungo come x con i relativi errori di ogni misura

#Calcolo Statistico
S = []
EQM = []
EM = []
PESI = []
for i in range (len(y)):
    h = n.abs(y[i]-medie[i]) #Modulo dello scostamento dalla media
    h1 = n.abs(y1[i]-medie[i])
    h2 = n.abs(y2[i]-medie[i])
    h3 = n.abs(y3[i]-medie[i])
    h4 = n.abs(y4[i]-medie[i])
    
    s = n.sqrt(((h+h1+h2+h3+h4)**2)/5) #Scarto Quadratico Medio
    S.append(s)

    peso = 1/(s**2) #Peso degli errori nella polyfit
    PESI.append(peso)

    eqm = s**2  #Errore Quadratico Medio
    EQM.append(eqm)
    
    em = s/n.sqrt(5) #Errore della Media
    EM.append(em)

    #print("misura: ",medie[i]," errore: ", s," e.q.m: ", eqm," errore della media: ",em)


#Creo La Parabola e la retta di bestfit, con gli errori
p = n.polyfit(x, medie, 2, w=PESI)
z = p[2]+p[1]*x+p[0]*x**2   #Parabola Bestfit già pesata
d = p[1]+2*p[0]*x     #Derivata Parabola 

#Plotto il tutto
plt.plot(x, medie, label="punti medi")
plt.plot(x, z, label="Parabola Bestfit")
plt.plot(x, d, label="Derivata (velocità)")

#Controllo che le velocità medie ogni 10 secondi siano
#equivalgano alle velocità istantanee alla metà degli intervalli
v = []  #velocità medie
tempi = []
for i in range(30,len(x),30):
    vm = ((medie[i]-medie[i-30])/(x[i]-x[i-30]))
    v.append(vm)
    tempi.append(x[i-15])
plt.plot(tempi, v, label="velocità medie")

vt = []   #Velocità istantanee a t = 30/2
for i in range(15,len(d),30):
    vt.append(d[i])

print("confronto tra velocità medie e istantanee:")
for i in range(len(v)):     #Confronto ad occhio che v == vt
    print(v[i],vt[i])

sumx = n.sum(tempi)     #Calcolo dei coefficienti A, B
sumy = n.sum(v)
sumx2 = sumx**2
sumxy = sumx*sumy
N = len(tempi)
delta = N*sumx2-sumx**2

A = (sumx2*sumy-sumx*sumxy)/delta
B = (N*sumxy-sumx*sumy)/delta

somme = []          #Per calcolare sigma, serve una sommatoria.
                    #è l'unico modo per farlo
for i in range(N):
    so = (v[i]-A-B*tempi[i])**2
    somme.append(so)
sommatoria = n.sum(somme)

sigmay = n.sqrt((1/(N-2))*sommatoria)
sigmab = sigmay*n.sqrt(N/delta) #b è il coefficiente angolare della retta
                                #ovvero l'accelerazione

sigmaalpha = 0.00145
g = 2*p[0]/(n.sin(0.004363323))
sigmag = n.sqrt((g**2)*((sigmab**2/B**2)+(sigmaalpha**2/n.tan(0.004363323)**2)))

print('g =',2*p[0]/(n.sin(0.004363323))) #Calcolo Effettivo accelerazione di gravità
print("errore di g: ",sigmag)
"""
g = 8.91410268302
errore di g:  2.96378281633
errore relativo: 33%
"""
plt.legend()
plt.show()
zac
