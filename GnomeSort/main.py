import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
from random import shuffle

mpl.use('Agg')

def desenhaGrafico(x, y, figura, xLabel ="Entradas", yLabel ="Saídas"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x, y, label ="Lista aleatória")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yLabel)
    plt.xlabel(xLabel)
    plt.savefig(figura)

def geraLista(tamanho):
    lista = list(range(1, tamanho + 1))
    shuffle(lista)
    return lista

def gnomesort(lista):
    tamanho = len(lista)
    indice = 0
    while indice < tamanho:
        if indice == 0:
            indice = indice + 1
        if lista[indice] >= lista[indice - 1]:
            indice = indice + 1
        else:
            aux = lista[indice]
            lista[indice] = lista[indice-1]
            lista[indice-1] = aux
            indice = indice - 1
    return lista

tamanho = [100000, 200000, 400000, 500000, 1000000, 2000000]
tempo = []

for i in range(6):
    lista = geraLista(tamanho[i])
    tempo.append(timeit.timeit("gnomesort({})".format(lista), setup="from __main__ import gnomesort", number=1))

desenhaGrafico(tamanho, tempo, "Tempo.png", 'Tamanho da lista de números', 'Tempo para ordenar pelo método')
