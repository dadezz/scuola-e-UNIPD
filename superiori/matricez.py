def sommaDiagPrinc(x):
    somma=0
    for i in range (len(x)):
        somma=somma+x[i][i]
    return somma

x=[[1,2,3],[4,5,6],[7,8,9]]
print(sommaDiagPrinc(x))
