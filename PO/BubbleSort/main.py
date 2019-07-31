import timeit
from random import randint
import matplotlib.pyplot as plt

def geraLista(tam):
    lista = []
    while len(lista) < tam:
        n = randint(1,1*tam)
        if n not in lista: lista.append(n)
    return lista

def desenhaGrafico(x,BSort,xl = "Entradas", yl = "loops",nam="img"):
    fig = plt.figure(figsize=(10, 13))
    ax = fig.add_subplot(111)
    ax.plot(x,BSort, label = "Bubble Sort")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.savefig(nam)

def bubbleSort(arr):
    count = 0
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            count+=1
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return count
  
lista = [10000,20000,50000,100000]
saidaB = []
saidaL = []


for i in range(len(lista)):
  saidaB.append(timeit.timeit("bubbleSort({})".format(geraLista(lista[i])),setup="from __main__ import geraLista,bubbleSort",number=1))

desenhaGrafico(lista,saidaB,nam="tempo")

for i in range(len(lista)):

  saidaL.append(bubbleSort(geraLista(lista[i])))

desenhaGrafico(lista,saidaL,nam="cont")
