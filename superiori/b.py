mat=[[1,2,3],[4,5,6],[7,8,9]]
s1=0
s=0

for i in range (len(mat)-1):
    s1+=mat[i][i]
for j in range(len(mat)-1,0,-1):
    s+=mat[j][j]
    
if s1==s:
    print("sdp=sds")
else:
    print("niente")
