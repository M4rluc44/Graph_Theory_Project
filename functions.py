def floyd_warshall(graph):
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            for k in range(len(graph[i])):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
    to_zero(graph)
    return graph

def to_zero(graph):
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            if graph[i][j] == float('Inf'):
                graph[i][j] = 0


#def cycles(graph):
