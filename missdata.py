import numpy as np
import matplotlib.pyplot as plt

dados = np.loadtxt("alunos.txt")
sapatos = dados[:,2]
altura = dados[:,0]
missdata = np.where(sapatos < 0)

def por40():
    dados = np.loadtxt("alunos.txt")
    sapatos = dados[:,2]

    sapatos[missdata] = 40

    print( sapatos)

def sapatosM ():
    dados = np.loadtxt("alunos.txt")
    sapatos = dados[:,2]

    sapatos[missdata] = np.mean(sapatos)
    print(sapatos)

def sapatosAlt():
    dados = np.loadtxt("alunos.txt")
    for elem in missdata[0]:
        if(altura[missdata][0] > 175):
            sapatos[elem] = 42
        else:
            sapatos[elem] = 39
    
    print (sapatos[missdata])



sapatosAlt()
print("")
print(altura[missdata])

