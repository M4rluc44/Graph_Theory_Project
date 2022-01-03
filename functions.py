from copy import deepcopy
import math
Inf = math.inf
maxsize = 100000000


# Floyd Warshall algorithm, displaying all needed arrays and returning the matrix P, showing the predecesor
# of each vertex (the matrix P, the adjency matrix)
def floyd_warshall(graph_test):
    # We make deepcopy or we have problems with array modification (not able to run the algo again for
    # example
    graph = deepcopy(graph_test)
    P = deepcopy(graph_test)

    for o in range(len(graph)):
        if graph[o][o] is not None:
            if graph[o][o] < 0:
                return False

    # begin of table initialization
    for m in range(len(P)):
        for n in range(len(P[m])):
            if graph[m][n] is not None:
                P[m][n] = m
                graph[m][n] = graph_test[m][n]
            elif m == n:
                P[m][n] = m
            else:
                graph[m][n] = Inf

    for m in range(len(P)):
        for n in range(len(P[m])):
            if graph_test[m][n] is None:
                graph_test[m][n] = Inf

    for m in range(len(P)):
        print("")
        graph[m][m] = min(0, graph_test[n][n])
    # End of table initialization

    # Initial tables
    print('Initial table P')
    display_table(P)
    print("\n")
    print("Initial table L")
    display_table(graph)
    # End of initial tables

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
        print("\n\nItération n°", i + 1, " table L : ", end=' ')
        display_table(graph)
        # Fin affichage table L

        # On affiche la table P ici
        print("\n\nItération n°", i + 1, " table P : ", end=' ')
        display_table(P)
        # Fin affichage table P
    print("\n\nWe end here at the iteration n°", i + 1, " with final tables P and L above\n")
    to_float(P)
    return P


# Change all Infinity to zero after doing the calculation
def to_float(graph):
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] is None:
                graph[i][j] = maxsize

# Display the table of a graph
def display_table(graph):
    for i in range(len(graph)):
        print("")
        for j in range(len(graph[i])):
            print(graph[i][j], "|", end=' ')


# to display the shortest path between two vertex (u the first and v the final)

def display_path(graph, u, v):
    route = [v]
    printPath(graph, v, u, route)
    print(f'The shortest path from {v} —> {u} is  ', end="")
    for i in range(len(route)):
        print(route[i], "-> ", end="")
    print(u)


def printPath(path, v, u, route):
    print("u : ", u, " v: ", v)
    if path[v][u] == v:
        return
    printPath(path, v, path[v][u], route)
    route.append(path[v][u])
