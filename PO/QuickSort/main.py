import random
import timeit
import matplotlib.pyplot as plt

def desenha_grafico(x, y, file_name, label1, xl="Entradas", yl="Saídas"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x, y, label=label1)
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig(file_name)

def particao(lista, ini, fim):
    pivo = lista[fim - 1]
    for i in range(ini, fim):
        if not lista[i] > pivo:
            lista[ini], lista[i] = lista[i], lista[ini]
            ini += 1
    return ini-1

def quick_sort(lista, ini, fim):
    if ini < fim:
        pivo = escolhe_pivo_aleatorio(lista, ini, fim)
        quick_sort(lista, ini, pivo)
        quick_sort(lista, pivo + 1, fim)
    return lista

def escolhe_pivo_aleatorio(lista, ini, fim):
    rand = random.randrange(ini, fim)
    lista[fim - 1], lista[rand] = lista[rand], lista[fim - 1]
    return particao(lista, ini, fim)

tam = [100000, 200000, 400000, 500000, 1000000, 2000000]
times = []

for i in range(len(tam)):
    lista_invertida = list(range(tam[i], 0, -1))
    times.append(timeit.timeit("quick_sort({}, {}, {})".format(lista_invertida, 0, len(lista_invertida)),
                               setup="from __main__ import quick_sort, escolhe_pivo_aleatorio, particao", number=1))

desenha_grafico(tam, times, "GraficoTempo.png", "Tempo gasto pelo quick_sort", xl="Tamanho da lista", yl="Tempo")
