from copy import deepcopy
import math
Inf = math.inf

# Floyd Warshall algorithm, displaying all needed arrays and returning the matrix P, showing the predecesor
# of each vertex (the matrix P, the adjency matrix)
def floyd_warshall(graph_test):
    # We make deepcopy or we have problems with array modification (not able to run the algo again for
    # example
    to_none(graph_test) # du to problem with deepcopy, needed when the user do another graph
    graph = deepcopy(graph_test)
    P = deepcopy(graph_test)
    table_p = []
    table_l = []

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
        graph[m][m] = min(0, graph_test[n][n])
    # End of table initialization

    # Initial tables storage
    table_p.append(deepcopy(P))
    table_l.append(deepcopy(graph))
    # End of initial tables storage

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

        # On store la table L
        table_l.append(graph)
        # Fin storage table L

        # On store la table P ici
        table_p.append(deepcopy(P))
        # Fin store table P

    for i in range(len(table_p)):
        if i == 0:
            print('\n\nInitial table L')
            display_table(table_l[i])
            print("\n\nInitial table P")
            display_table(table_p[i])
        else:
            print("\n\nItération n°", i, " table L : ", end=' ')
            display_table(table_l[i])
            print("\n\nItération n°", i, " table P : ", end=' ')
            display_table(table_p[i])

    print("\n\nWe end here at the iteration n°", i + 1, " with final tables P and L above")

    return P


# Change all Infinity to zero after doing the calculation
def to_none(graph):
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] is Inf:
                graph[i][j] = None

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
