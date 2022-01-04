def g(n):
    if n<2:
        return 1
    else:
        return g(n-1)+1/(n-1)

n=2
while (n<=200):
    print (n, g(n))
    n+=2


##############   SOLUZIONE  ################
#def succ(n):
#    i=0
#    while (i<n):
#        if (i<2):
#            g=1
#            if i%2==0:
#                print (i, g)
#        else:
#            g=g+1/(i-1)
#            if i%2==0:
#                print i, g
#        i+=1
