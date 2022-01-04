# 1 piede = 0.3048 metri
#inizio= 0 centimetri e fine = 30 centimetri, passo = 2 cm

m = 0
#i centimetri vanno divisi per diventare piedi
centimetri=[]
piedi=[]
while m <= 0.3:
    centimetro = int(m*100)
    piede = m/0.3048
    piedi.append(piede)
    centimetri.append(centimetro)
    m+=0.02

print(centimetri)
print(piedi)
