#stampa “sparsa” se il numero degli elementi non nulli è inferiore al 5% del numero degli
#elementi totali.
mat=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,9],[0,0,0,0,0],[0,0,0,0,0]]
cont=0
for i in range (len(mat)):
    for j in range (len(mat[0])):
        if mat[i][j]!=0:
            cont+=1
ntot=len(mat)*len(mat[0])
if 100*cont/ntot<5:
    print("sparsa")
else:
    print ("no")
