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

#calcolo coefficienti rette ed errori
#uso una funzione, che richiamerò ogni volta per evitare ripetizioni
def minimi (x,y):
    N = len(x)
    sumx = 0
    sumx2 = 0
    sumxy = 0
    sumy = 0

    for j in range(N):
        sumx = sumx+x[j]
        sumx2 = sumx2+x[j]**2
        sumxy = sumxy+x[j]*y[j]
        sumy = sumy+y[j]
        
    D = N*sumx2-sumx**2
    B = (N*sumxy-sumx*sumy)/D
    A = (sumy-B*sumx)/N

    somme = 0      #calcolo errori dei coefficienti
    for i in range(1, N):
        somme += (y[i]-A-B*x[i])**2
        
    sigmay = np.sqrt((1/(N-2))*somme)
    sigmab = sigmay*np.sqrt(N/D) #errore sul coefficiente b
    sigmaa = sigmay*np.sqrt(sumx2/D) #errore sul coefficiente a
    
    return(A,B, sigmay,sigmab,sigmaa)

#CREO UNA MATRICE CHE ABBIA PER OGNI RIGA UNA LISTA CON I VALORI DEI TEMPI DI TUTTI I FILE PER OGNI GIRO
#Accelerazione
mat=[]
for i in range (len(dat1)):
    mat.append([val1[i], val2[i], val3[i], val4[i], val5[i], val6[i], val7[i], val8[i], val9[i], val10[i]])
#Decelerazione
mat2=[]
for i in range (6):
    mat2.append([dec1[i], dec2[i], dec3[i], dec4[i], dec5[i], dec6[i], dec7[i], dec8[i], dec9[i], dec10[i]])

#CALCOLO LE MEDIE DEI TEMPI DI PERCORRENZA PER OGNI GIRO
#Accelerazione
tempi_singologiro_acc=[]
for i in range (len(mat)):
    media=np.mean(mat[i])
    tempi_singologiro_acc.append(media)
#Decelerazione
tempi_singologiro_dec=[]
for i in range (len(mat2)):
    media=np.mean(mat2[i])
    tempi_singologiro_dec.append(media)

#deviazione standard valori
deviazioni = []
for i in range (len(mat)):
    n = len (mat[i])
    d = []
    for j in range (len(mat[i])):
        d1 = mat[i]-tempi_singologiro_acc[i]
        d1 = d1**2
        d.append(d1)
    dev = (1/n)*np.sum(d)
    deviazioni.append(dev)

#CALCOLO I TEMPI A METÀ DELL'INTERVALLO (SERVONO PER LE V IST)
#Accelerazione
tempi=[]
for i in range (len(tempi_singologiro_acc)):
    tempo=np.sum(tempi_singologiro_acc[:i+1])/2
    tempi.append(tempo)
#Decelerazione
tempidec=[]
for i in range (len(tempi_singologiro_dec)):
    tempo=(np.sum(tempi_singologiro_acc)+np.sum(tempi_singologiro_dec[:i+1]))/2
    tempidec.append(tempo)


#CALCOLO LE VELOCITÀ MEDIE ANGOLARI PER IL GIRO I-ESIMO
#Accelerazione
velmedie=[]
for i in range (len(tempi_singologiro_acc)):
    velmedia=((i+1)*2*np.pi)/np.sum(tempi_singologiro_acc[:i+1])
    velmedie.append(velmedia)
#Decelerazione
velmedie2=[]
for i in range (len(tempi_singologiro_dec)):
    velmedia=((i+1)*2*10*np.pi)/np.sum(tempi_singologiro_dec[:i+1])
    velmedie2.append(velmedia)

################### RETTA ACC (tempi, velmedie) ########################
A_acc1, B_acc1, sigmay_acc1, sigmab_acc1, sigmaa_acc1 = minimi(tempi, velmedie)
print("RETTA ACCELERAZIONI y = A+Bx:")
print("A: ", A_acc1)
print("B: ", B_acc1)
print("sigma y: ", sigmay_acc1)
print("sigma b: ", sigmab_acc1)
print("sigma a: ", sigmaa_acc1)
tempi = np.float64(tempi)
zacc1 = A_acc1+B_acc1*tempi

################### RETTA DEC (tempi, velmedie) ########################
A_dec, B_dec, sigmay_dec, sigmab_dec, sigmaa_dec = minimi(tempidec, velmedie2)
print("")
print("RETTA DECELERAZIONI y = A+Bx:")
print("A: ", A_dec)
print("B: ", B_dec)
print("sigma y: ", sigmay_dec)
print("sigma b: ", sigmab_dec)
print("sigma a: ", sigmaa_dec)
tempidec = np.float64(tempidec)
zdec = A_dec+B_dec*tempidec

#definisco le costanti:
m = 0.034   #Kg
r = 0.01895 #m
g = 9.806   #m/s^2

I = ((m*r*g)-(B_acc1*m*r*r))/(B_acc1-B_dec)
Momento = -(B_dec*I)

"""
##################  PROVIAMO ORA A USARE IL SECONDO METODO  #####################
"""

#creo un array con il numero di giri (quindi 1, 2, 3, 4, 5, 6 etc)
tempi_secondo_metodo=[]
for i in range (len(tempi_singologiro_acc)):
    tempo=np.sum(tempi_singologiro_acc[:i+1])
    tempi_secondo_metodo.append(tempo)

n = []
for i in range(len(tempi_secondo_metodo)):
    valore = np.sqrt(i+1)
    n.append(valore)

################### RETTA METODO2 (n, tempi) ########################
A_acc2, B_acc2, sigmay_acc2, sigmab_acc2, sigmaa_acc2 = minimi(n, tempi_secondo_metodo)
print(" ")
print("RETTA ACCELERAZIONI metodo2 y = A+Bx:")
print("A: ", A_acc2)
print("B: ", B_acc2)
print("sigma y: ", sigmay_acc2)
print("sigma b: ", sigmab_acc2)
print("sigma a: ", sigmaa_acc2)
n = np.float64(n)
zacc2 = A_acc2+B_acc2*n

I_secondo = (m*r*(g*B_acc2**2 - 4*np.pi*r))/(4*np.pi - B_dec*B_acc2**2)
Momento_secondo = -(B_dec*I_secondo)

print(" ")
print("primo metodo")
print("Inerzia: ",I)
print("Attrito: ",Momento)
print("secondo metodo")
print("Inerzia: ",I_secondo)
print("Attrito: ",Momento_secondo)

"""
############################  PLOT VARI  ################################
"""

#plt.plot(tempi, velmedie, ".k", label="velocità medie in accelerazione")
#plt.plot(tempi, zacc1, "y", label="retta polyfit accelerazioni")
#plt.plot(tempidec, velmedie2, ".r", label="velocità medie in decelerazione")
#plt.plot(tempidec, zdec, "aquamarine", label="retta polyfit decelerazione")
plt.plot(n, tempi_secondo_metodo, ".b", label="relazione numero di giri e tempi")
plt.plot(n, zacc2, label="retta polyfit")
plt.xlabel("Radice del numero di giri")
plt.ylabel("Tempi [s]")
plt.legend()
#plt.show()


