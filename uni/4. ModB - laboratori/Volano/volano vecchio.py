import numpy as np
import matplotlib.pyplot as plt

#IMPORTO I DATI
dat1=np.genfromtxt("volano1.txt")
dat2=np.genfromtxt("volano2.txt")
dat3=np.genfromtxt("volano3.txt")
dat4=np.genfromtxt("volano4.txt")
dat5=np.genfromtxt("volano5.txt")
dat6=np.genfromtxt("volano6.txt")
dat7=np.genfromtxt("volano7.txt")
dat8=np.genfromtxt("volano8.txt")
dat9=np.genfromtxt("volano9.txt")
dat10=np.genfromtxt("volano10.txt")

#TEMPI DURANTE LE ACCELERAZIONI
val1=dat1[:,0]
val2=dat2[:,0]
val3=dat3[:,0]
val4=dat4[:,0]
val5=dat5[:,0]
val6=dat6[:,0]
val7=dat7[:,0]
val8=dat8[:,0]
val9=dat9[:,0]
val10=dat10[:,0]

#TEMPI DURANTE LE DECELERAZIONI
dec1=dat1[:,1]
dec2=dat2[:,1]
dec3=dat3[:,1]
dec4=dat4[:,1]
dec5=dat5[:,1]
dec6=dat6[:,1]
dec7=dat7[:,1]
dec8=dat8[:,1]
dec9=dat9[:,1]
dec10=dat10[:,1]

#CREO UNA MATRICE CHE ABBIA PER OGNI RIGA UNA LISTA CON I VALORI DEI TEMPI DI TUTTI I FILE PER OGNI GIRO
#ACCELERAZIONE
mat=[]
for i in range (len(dat1)):
    mat.append([val1[i], val2[i], val3[i], val4[i], val5[i], val6[i], val7[i], val8[i], val9[i], val10[i]])
    #print(mat[i])

#print(" ")  #è SOLO UN SEPARATORE VISIVO

#DECELERAZIONE
mat2=[]
for i in range (6):
    mat2.append([dec1[i], dec2[i], dec3[i], dec4[i], dec5[i], dec6[i], dec7[i], dec8[i], dec9[i], dec10[i]])
    #print(mat2[i])

#CALCOLO LE MEDIE DEI TEMPI DI PERCORRENZA PER OGNI GIRO
#ACCELERAZIONE
medieac=[]
for i in range (len(mat)):
    media=np.mean(mat[i])
    medieac.append(media)
medieacc=medieac#[::-1]

tempi=[]    #calcolo i tempi relativi alle velocità istantanee (quindi a metà
#dell'intervallo) sull'accelerazione
for i in range (len(medieacc)):
    tempo=np.sum(medieacc[:i+1])/2
    tempi.append(tempo)

#print("tempi accelerazioni", tempi) ##############ATTENTI COPIARE DU DEC
#DECELERAZIONE
mediede=[]
for i in range (len(mat2)):
    media=np.mean(mat2[i])
    mediede.append(media)
mediedec=mediede#[::-1]

#CALCOLO LE VELOCITà MEDIE ANGOLARI PER IL GIRO I-ESIMO
#ACCELERAZIONE
velmedie=[]
for i in range (len(medieacc)):
    velmedia=(2*np.pi)/medieacc[i]
    velmedie.append(velmedia)


tempidec=[] #calcolo i tempi come prima, sulla decelerazione
for i in range (len(mediedec)):
    tempo=(np.sum(medieacc)+np.sum(mediedec[:i+1]))/2
    tempidec.append(tempo)

#print("tempi decelerazioni", tempidec)

#DECELERAZIONE
velmedie2=[]
for i in range (len(mediedec)):
    velmedia=(2*10*np.pi)/mediedec[i]
    velmedie2.append(velmedia)

"""
sappiamo che
velmedie(t) = [alfa]*t
dove alfa = (mrg-Momentoattrito)/(I+mr^2)   -> NE RICAVO I.
per farlo uso la fase di accelerazione.

mi manca però conoscere il momento delle forze di attrito, per cui uso la fase
di decelerazione. infatti,
velmedie2(t) = velmedie[più grande]+(beta)*t
dove beta = -(Momentoattrito/I)

ora che ho alfa e beta, posso trovare
I = (mrg-alfa*m*r^2)/(alfa-beta)
"""

tempi = np.float64(tempi) #conversione in float64 dei dati (serve per polyfit)
velmedie = np.float64(velmedie)
tempidec = np.float64(tempidec)
velmedie2 = np.float64(velmedie2)
pacc = np.polyfit(tempi, velmedie, 1) #retta polyfit accelerazioni
zacc = pacc[1]+pacc[0]*tempi
pdec = np.polyfit(tempidec, velmedie2, 1) #retta polyfit decelerazioni
zdec = pdec[1]+pdec[0]*tempidec

"""
AVENDO LE RETTE, I DUE COEFFICIENTI ANGOLARI SONO ALFA E BETA
"""
alfa = pacc[0]
beta = pdec[0]

#definisco le costanti:
m = 0.034   #Kg
r = 0.01895 #m
g = 9.806   #m/s^2

I = ((m*r*g)-(alfa*m*r*r))/(alfa-beta)
Momento = -(beta*I)

print("Inerzia: ",I)
print("Attrito: ",Momento)

#print(" ")
#print(medieacc)
#print(mediedec)
#print(" ")
#print(velmedie)
#print(velmedie2)


"""
PROVIAMO ORA A USARE IL SECONDO METODO
"""
#creo un array con il numero di giri (quindi 1, 2, 3, 4, 5, 6 etc)
n = []
for i in range(len(tempi)):
    valore = np.sqrt(i+1)
    n.append(valore)
n = np.float64(n)

pn = np.polyfit(n, tempi, 1) #retta polyfit tempi rispetto a n
zn = pn[1]+pn[0]*n  #l'equazione è t = t0 + theta*n
theta = pn[0]

I_secondo = (m*r*(g*theta*theta - 4*np.pi*r))/(4*np.pi - beta*theta*theta)
Momento_secondo = -(beta*I_secondo)
print("Inerzia: ",I_secondo)
print("Attrito: ",Momento_secondo)

#plt.plot(n, tempi, ".b", label="relazione numero di giri e tempi")
#plt.plot(n, zn, label="retta polyfit secondo metodo")
plt.plot(tempi, velmedie, ".k", label="velocità medie in accelerazione")
plt.plot(tempi, zacc, "y", label="retta polyfit accelerazioni")
plt.plot(tempidec, velmedie2, ".r", label="velocità medie in accelerazione")
plt.plot(tempidec, zdec, "aquamarine", label="retta polyfit decelerazione")
plt.legend()
plt.show()


