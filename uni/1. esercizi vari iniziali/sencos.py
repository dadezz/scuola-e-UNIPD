from matplotlib.pyplot import *
from math import *

def funz (a, xmin, xmax, n):
    incx=(xmax-xmin)/(n-1)
    listax = []
    listay = []
    for i in range (n):
        x=xmin+incx*i
        y=sin(x)+a*cos(x**2)
        listax.append(x)
        listay.append(y)

    plot (listax,listay)
    show()

