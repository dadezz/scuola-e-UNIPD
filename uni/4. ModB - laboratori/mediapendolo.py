import numpy as n
import matplotlib.pyplot as plt

dat=n.genfromtxt('C:/Users/utente/OneDrive/Desktop/Finale.txt')

media=n.mean(dat)
errore=n.std(dat)/n.sqrt(5)

print(media)
print(errore)

#2.0008799999999995      media
#0.0001863330351816057  errore della media 
