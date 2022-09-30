"""
a, c, f, g, h, l, m, q, r, s, t, u, w, x
"""

"""
18
FALSE
"""

"""
a string
b float
c int
d complex
e string
f int
"""

"""
a 7
b 8
c 15
d 7
e 262144 ou 4096
f 6
"""

"""
2.2.5

a  2+(3*(6/2)) = 11
b (4+6)/(2+3) = 2
c (4/2)**5 = 32
d (4/2)**(5+1) = 64
e (-3)**2 = 9
f -(3**2) = -9

"""

"""
2.2.6
a float 
b float
c float
d float
e float
f float
g complex
h complex
i complex
j float
k float
l float
"""

"""
2.2.7
a 4.115100000000002
b 795
c 30
d 0.9375
"""

"""
2.2.8

"""
import math
import arqui

def calcular(x):
    print( x**4 + x**3 + 2*x**2 - x)
    

#calculo de arquimedes para PI

arqui.arqui()
#volume de um cone quaquer

def cone():
    r = float(input('digite o raio (m) \r'))
    h = float(input('digite a altura (m) \r'))
    pi = math.pi
    
    print ( pi*r**2*h/3 )
