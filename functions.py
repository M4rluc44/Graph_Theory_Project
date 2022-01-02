from copy import deepcopy
import math
Inf = math.inf

# Floyd Warshall algorithm, displaying all needed arrays and returning the matrix P, showing the predecesor
# of each vertex (the matrix P, the adjency matrix)
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
                return False

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

# Change all Infinity to zero after doing the calculation
def to_zero(graph):
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] == float('Inf'):
                graph[i][j] = 0

# Display the table of a graph
def display_table(graph):
    for i in range(len(graph)):
        print("")
        for j in range(len(graph[i])):
            print(graph[i][j], "|", end=' ')

# function to display the graph with design, not very useful
def display_graph(graph):
    import matplotlib.pyplot as plt
    import networkx as nx
    import numpy as np

    G = nx.DiGraph()
    for i in range(len(graph)):
        for j in range(len(graph)):
            if graph[i][j] == 1:
                G.add_edge(i, j)
    nx.draw(G)
    plt.show()

            # to display the shortest path between two vertex (u the first and v the final)
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