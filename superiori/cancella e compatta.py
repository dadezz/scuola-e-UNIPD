def CancellaeCompatta(v,i,s):
    for j in range(len(v)):
        if v[j]!=v[i]:
            s.append(v[j])
    return s

v=[4,6,1,18,45]
i=3
s=[]
print(CancellaeCompatta(v,i,s))
