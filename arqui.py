import math
def arqui():
    n = int(input('digite o numero de lados \n'))
    ang = math.radians( 180/n )
    sin = math.sin(ang)
    P = 2*n*sin
    print (P/2)
