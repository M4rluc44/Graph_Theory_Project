from copy import deepcopy
import math
Inf = math.inf

def floyd_warshall(graph):

    P = deepcopy(graph)
    for m in range(len(P)):
        print("")
        for n in range(len(P[m])):
            if P[m][n] != Inf:
                P[m][n] = m + 1

    for i in range(len(graph)):
        for j in range(len(graph[i])):
            for k in range(len(graph[i])):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
                    P[i][j] = k

        # On affiche la table L
        print("\nItération n°", i, " table L : ", end=' ')
        display_table(graph)
        # Fin affichage table L

        # On affiche la table P ici
        print("\n\nItération n°", i, " table P : ", end=' ')
        display_table(P)
        # Fin affichage table P

    to_zero(graph)
    return graph

def to_zero(graph):
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] == float('Inf'):
                graph[i][j] = 0

def display_table(graph):
    for i in range(len(graph)):
        print("")
        for j in range(len(graph[i])):
            print(graph[i][j], "|", end=' ')

def display_graph(graph):
    import matplotlib.pyplot as plt
    import networkx as nx
    import numpy as np

    G = nx.from_numpy_matrix(np.array(graph))
    nx.draw(G, with_labels=True)
    plt.show()

#def cycles(graph):
