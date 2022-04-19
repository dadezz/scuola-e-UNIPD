#FUSIONE DI DUE STRINGHE ORDINATE CON METODO MERGE
s="abcdefhirstuvz"
a="efghilmnopq"
i=0
j=0
s3=""
if len(s)<len(a):
    aux=s
    s=a
    a=aux
while i<=len(s)-1 and j<=len(a)-1:
    if s[i]<a[j]:
        s3=s3+s[i]
        i=i+1
    else:
        s3=s3+a[j]
        j=j+1
print(s3,s[i:])   







