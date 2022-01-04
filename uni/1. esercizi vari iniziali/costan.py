from matplotlib.pyplot import *
from math import *

def funz (a, xmin, xmax, n):
    incx=(xmax-xmin)/(n-1)
    lx = []
    ly = []
    for i in range (n):
        x=xmin+incx*i
        y=a*(cos(tan(x)))
        lx.append(x)
        ly.append(y)
    plot (lx,ly)
    show()
