def sommaDiagPrinc(mat):
    s=0
    for i in range (len(mat)):
        s+=mat[i][i]
    return s

mat=[[1,2,3],[4,5,6],[7,8,9]]
print(sommaDiagPrinc(mat))
