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

def heapsort(lista):
    for i in range(len(lista), -1, -1):
        distribuir(lista, len(lista), i)

    for i in range(len(lista)-1, 0, -1):
        aux = lista[i]
        lista[i] = lista[0]
        lista[0] = aux
        distribuir(lista, i, 0)

def distribuir(lista, tamanho, atual):
    maior = atual
    esquerdo = 2 * atual + 1
    direito = 2 * atual + 2

    if esquerdo < tamanho and lista[atual] < lista[esquerdo]:
        maior = esquerdo

    if direito < tamanho and lista[maior] < lista[direito]:
        maior = direito

    if maior != atual:
        aux = lista[atual]
        lista[atual] = lista[maior]
        lista[maior] = aux
        distribuir(lista, tamanho, maior)

tamanho = [100000, 200000, 400000, 500000, 1000000, 2000000]
tempo = []

for i in range(6):
    lista = geraLista(tamanho[i])
    tempo.append(timeit.timeit("heapsort({})".format(lista), setup="from __main__ import heapsort", number=1))

desenhaGrafico(tamanho, tempo, "Tempo.png", 'Tamanho da lista de números', 'Tempo para ordenar pelo método')
