import timeit
from random import randint, shuffle
import matplotlib.pyplot as plt

def desenhaGrafico(x,lista1,xl = "Entradas", yl = "Y",name="out", label1 = "Lista 1", label2 = "Lista 2"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x, lista1, label = label1)
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.savefig(name)

def geraLista(tam):
    lista = list(range(1, tam + 1))
    shuffle(lista)
    return lista

def sort(lista, maximo):
    count(lista, maximo)

def count(lista, maximo):
	count = [0] * (maximo+1)
	listaOrdenada = [None] * len(lista)
	for i in range(len(lista)):
		count[lista[i]] += 1
	for i in range(1, maximo+1):
		count[i] += count[i-1] 
	for i in range(len(lista)):
		listaOrdenada[count[lista[i]]-1] = lista[i]
		count[lista[i]] -= 1

quant = [100000,200000,400000,500000,1000000,2000000]
graf_tempo = []

for i in range(len(quant)):
    print(quant[i])
    lista = geraLista(quant[i])
    graf_tempo.append(timeit.timeit("sort({},{})".format(lista, quant[i]),setup="from __main__ import sort",number=1))

desenhaGrafico(quant,graf_tempo,"Tamanho", "Tempo", "Tempo", label1 = "Lista")
