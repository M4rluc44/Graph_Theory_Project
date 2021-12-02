def floyd_warshall(graph):
    for i in range(len(graph)):
        for j in range(len(graph[i])):
            for k in range(len(graph[i])):
                if graph[i][j] == 'Inf' and graph[i][k] == 'Inf' and graph[k][j] != 'Inf':
                    graph[i][j] = graph[k][j]
                elif graph[i][j] == 'Inf' and graph[k][j] == 'Inf' and graph[i][k] != 'Inf':
                    graph[i][j] = graph[i][k]
                elif graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]

    return graph

