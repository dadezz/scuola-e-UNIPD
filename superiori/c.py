#stampa “triangolare alta” se tutti gli elementi al di sotto della diagonale principale sono a
#zero;
mat=[[0,2,3],[0,0,6],[0,0,0]]
conttot=0
contzero=0
for i in range(len(mat)):
    for j in range (i+1):
        conttot+=1
        if mat[i][j]==0:
            contzero+=1
if contzero==conttot:
    print("triangolare alta")
else:
    print("niente")
