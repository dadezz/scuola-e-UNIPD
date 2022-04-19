#intersezione di due stringhe

s1=input("inserisci la prima stringa: ")
s2=input("inserisci la seconda: ")
x=len(s1)
s3=""

for i in range (0,x):
    if s1 [i] not in s1 [:i]:
        if s1[i] in s2:
            s3+=s1[i]
print(s3)
