#BUBBLE SORT: metodo di ordinamento
s=input("inserisci la stringa o la lista: ")
z=s
x=len(s)
def ordinabubble (s):
    for i in range (x-1, 0, -1):
        for j in range (1,i+1):
            if s[j-1]>s[j]:
                s=s[:j-1]+s[j]+s[j-1]+s[j+1:]
    return s
print("stringa ",z," ordinata con il metodo bubble sort: ",ordinabubble(s))
