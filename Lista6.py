#Lista de exercicios 6

#6.2
from re import I


def crescente(x, y, z):
    lista = (x, y, z)
    
    if x > y > z:
        print(z, y, x)

    elif x < y < z:
        print(lista)

    elif z < y < x:
        print(z, y, x)

    elif z < x < y:
        print(z, x, y)

    elif y < z < x:
        print(y, z, x)

    elif y < x < z:
        print(y, x, z)

#6.3
def autoestradas():
    estrada = input("Digite a autoestradas desejada: ")
    estrada = estrada.lower()

    if estrada == "a1":
        custo1 = (0.15*120) + 6.52
        print(f'O custo da viagem por essa rota será de {custo1}')

    elif estrada == "a20":
        custo2 = (0.12*120) + 15.3
        print(f'O custo da viagem por essa rota será de {custo2}')

    elif estrada == "a21":
        custo3 = (0.1*120) + 5.75
        print(f'O custo da viagem por essa rota será de {custo3}')

#6.4
def imposto():
    salario = int(input("Digite o seu salario: "))
    
    salario = 0.75*0.9*0.95*salario


    print(f'O seu salario final é de €{salario}')

#6.6
def troca():
    i = 20

    for i in range(20, -1, -2):
        print('i=', i)



if __name__ == "__main__":
    troca()