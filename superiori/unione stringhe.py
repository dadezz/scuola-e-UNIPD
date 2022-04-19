#UNIONE: unione di due stringhe senza ripetizioni

s1=input("inserisci la prima stringa: ")
s2=input("inserisci la seconda: ")
x=int(len(s1))
y=int(len(s2))
s3=""
for i in range (0,x):
    if s1[i] not in s1[:i]:
        s3+=s1[i]
for j in range (0,y):
    if s2[j] not in s2[:j]:
        if s2[j] not in s1:
            s3+=s2[j]
print (s3)
