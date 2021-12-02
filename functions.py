def floyd_warshall(graph):
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            for k in range(len(graph[i])):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]
    return graph

