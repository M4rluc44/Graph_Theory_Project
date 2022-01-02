from copy import deepcopy
import math
Inf = math.inf

def floyd_warshall(graph_test):
    # We make deepcopy or we have problems with array modification (not able to run the algo again for
    # example
    graph = deepcopy(graph_test)
    P = deepcopy(graph_test)

    print("je sui la copie")
    display_table(P)
    for m in range(len(P)):
        print("")
        for n in range(len(P[m])):
            if P[m][n] != Inf:
                P[m][n] = m

    for i in range(len(graph)):
        for j in range(len(graph[i])):
            for k in range(len(graph[i])):
                if graph[j][i] + graph[i][k] < graph[j][k]:
                    graph[j][k] = graph[j][i] + graph[i][k]
                    P[j][k] = P[i][k]

        # We check if there is an absorbent cycle
        for o in range(len(graph)):
            if graph[o][o] < 0:
                print("J'ai un cyle bg")

        # On affiche la table L
        print("\n\nItération n°", i+1, " table L : ", end=' ')
        display_table(graph)
        # Fin affichage table L

        # On affiche la table P ici
        print("\n\nItération n°", i+1, " table P : ", end=' ')
        display_table(P)
        # Fin affichage table P



    to_zero(graph)
    return P

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

# to display the shortest path between two vertex (u the first and v the final)
def paths(graph, u, v):
    buff = []
    path = ""
    last = u
    #while last != v:
    #    if graph[i][u] == last:
    #        print("Je suis là")
    for i in range(len(graph)):
        for j in range(len(graph[i])):

            if graph[u][j] == last:
                print("Je suis là")
                path += str(graph[u][j])
                last = j
            if last == v:
                path += str(v)
                return path
    return path

def display_path(graph, u, v):
    route = [v]
    printPath(graph, v, u, route)
    print(f'The shortest path from {v} —> {u} is  ', end="")
    for i in range(len(route)):
        print(route[i],"-> ", end="")
    print(u)

def printPath(path, v, u, route):
    if path[v][u] == v:
        return
    printPath(path, v, path[v][u], route)
    route.append(path[v][u])