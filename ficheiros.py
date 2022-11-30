#exercios da ficha 9 sobre ficheiros
import matplotlib.pyplot as plt
import random
import turtle as tt



#9.2
"""
meu_ficheiro = open('primeiro.txt', 'w+')

meu_ficheiro.write('Essa merda funciona?')
meu_ficheiro.close()
"""

#9.3 - Mostrar seq de caracteres pré definidos

def lerDesde(arquivo, pos):
    fich = open(arquivo, 'r')
    fich.seek(pos, 0)
    texto = fich.read()
    fich.close()

    return texto
    
#9.4
def AddData(arquivo,data):
    fich = open(arquivo,'a')
    fich.write(f'\n{data}')

    fich.close()

#9.5
def Listnum():
    lista = []
    with open('primeiro.txt', 'r') as arquivo:
        for linha in arquivo:
            for car in linha:
                try:
                    lista.append(int(car))
                except:
                    continue

    print(lista)

#9.6
def trasposta(matriz):
    return list(zip(*matriz))

def le_linha(fich):
    dado =[]
    with open(fich, 'r') as arquivo:
        linha = arquivo.readline()
        while(linha != '') and (linha =='\n'):
                linha = arquivo.readline()
        if linha == '':
                return -1
        else:
                linha = linha[:-1].split()
                return [float(dado) for dado in linha]


def GrafTemp():
    meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

    #Abre o Ficheiro
    with open('temperaturas.txt', 'r') as arquivo:
        linhas = arquivo.readlines()

        #Criando matriz das tempertaturas
        matriz = []
        for linha in linhas:
            medidas_str = linha[:-1].split()
            medidas = [float(medida) for medida in medidas_str]
            matriz.append(medidas)

        mydata = trasposta(matriz)

        #Guardadno as temperaturas maximas e minimas
        maxima = []
        minima = []

        for mes in mydata:
            maxima.append(max(mes))
            minima.append(min(mes))
        
        #Fazendo o grafico
        plt.plot(meses, maxima)
        plt.plot(meses, minima)
        plt.show()


#9.7 - copia um documento
def copia(original, copy):
    with open(f'{original}', 'r') as arquivo:

        novo = open(f'{copy}', 'w+')

        for linha in arquivo:
            novo.write(linha)
            

            
#9.8 - turtle com losiçoes aleatorias
def tutuga(coord):
    pos = ()
    ListPos = []
    arquivoW = open('turtle.txt','w+')

    #Cria as Coordenadas e escreve no ficheiro.
    for i in range(coord):
        pos = (f'{random.randint(1,6)}' + ' ' + f'{random.randint(1,6)}')
        arquivoW.write(f'{pos}\n')

    arquivoW.close()

    #Abre o arquivo em modo de leitura e trata a informação
    arquivoR = open('turtle.txt', 'r')
    
    for linha in arquivoR:

        a = int(linha[0])*10
        b = int(linha[2])*10

        ListPos.append((a,b))
    
    arquivoR.close()
    
    #Turtle
    tt.penup()
    tt.setpos(ListPos[0][0], ListPos[0][1])
    tt.pendown()

    for i in range(1,len(ListPos)):
        tt.setpos(ListPos[i][0], ListPos[i][1])

    tt.done()


#Criar ficheiros com numeros aleatorios
def CriaFichRandInt(arquivo,quant):
    with open(f'{arquivo}', 'w') as fich:
        for i in range(quant):
            pos = (f'{random.randint(1, 6)}' + ' ' + f'{random.randint(1, 6)}')
            fich.write(f'{pos}\n')


#Criar ficheiro para ler o arquivo
def LeFich(arquivo):
    
    listaVal = []

    with open(f'{arquivo}', 'r') as fich:

        valores = fich.readlines()

        for linha in valores:
            a = int(linha[0])
            b = int(linha[2])

            listaVal.append(a)
            listaVal.append(b)

        return listaVal


#9.9 - Frequencia de numeros
def count(arquivo,quant):
    dicio= {}

    #Cria o arquivo e escreve os numeros
    CriaFichRandInt(arquivo, quant)

    #Le o ficheiro e devlve uma lista com todos os numeros
    lista = LeFich(arquivo)

    #Trata os dados
    lista.sort()

    #Cria um dicionario com o numero e a ocorrencia
    for value in lista:
        if not value in dicio:
            dicio[value] = 0

        dicio[value] += 1
    
    #Varre o dicionario criando o grafico
    for k, v in dicio.items():

        plt.bar(k,v)
    
    plt.xlabel('Numero')
    plt.ylabel('Ocorrencia')
    plt.show()

#Le a lista e soma os numeros
def LeSoma(arquivo):
    listaSoma = []

    with open(f'{arquivo}', 'r') as fich:

        valores = fich.readlines()

        for linha in valores:
            a = int(linha[0])
            b = int(linha[2])

            listaSoma.append(a+b)
            

        return listaSoma

#9.10 - Porecentagem da soma de dois valores
def SomaPercent(arquivo, quant):
    dicioQuant = {}

    #Cria o arquivo e escreve os numeros
    CriaFichRandInt(arquivo, quant)

    #Le o ficheiro e devlve uma lista com todos os numeros
    lista = LeFich(arquivo)
    lista.sort()

    #Cria um dicionario com o numero e a ocorrencia
    for value in lista:
        if not value in dicioQuant:
            dicioQuant[value] = 0

        dicioQuant[value] += 1

    #Calcula a porcentagem e grafico
    for k, v in dicioQuant.items():
        perc = v/len(lista)

        
        plt.bar(k,perc)

    plt.xlabel('Numero')
    plt.ylabel('Porcentagem')
    plt.show()

SomaPercent('numeros.txt', 10)
    