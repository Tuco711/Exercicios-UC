#Exercicio 3.3.1 lista #B
"""
Homem = 2 esposas
Irmao = 3
tio = 4
"""
#Exercicio 3.3.1
"""
valor = 3 
id = 2543077648752
type = int

valor = 3.1
id = 2543078775440
type = float

valor = arroz
id = 2543084193008
type = string

"""
import math
import matplotlib.pyplot as plt

#Exercicio 3.3.3

def hamburger():
    L = 7.62
    R = 8.89/2
    areaC = math.pi*R**2
    areaQ = L**2
    
    if areaC > areaQ:
        print('pode reclamar!')

    else: print('nao pode reclamar, cala a boca')


#Exercicio 3.4.1
def arqui(lados):
    n = lados
    ang = math.radians( 180/n )
    sin = math.sin(ang)
    P = 2*n*sin
    pi = P/2

    return(pi)

for i in range(1,100):
    x = i
    y = arqui(i)

    plt.scatter(x, y, c= 'black')



#Exercicio 3.4.2
def cone():
    r = float(input('digite o raio (m) \r'))
    h = float(input('digite a altura (m) \r'))
    pi = math.pi
    
    print ( pi*r**2*h/3 )

#Exercicio 3.4.3

def fahrenheit(celcius):
    f = 9/5(celcius) + 32
    return f

for celcius in range(1, 20):
    x = celcius
    y = fahrenheit(celcius)

    plt.scatter(x, y)
plt.show()