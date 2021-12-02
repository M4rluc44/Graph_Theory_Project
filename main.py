import test_graph
import functions

result = functions.floyd_warshall(test_graph.graph_1)

for i in range(len(result)):
    print("")
    for j in range(len(result[i])):
        print(result[i][j], end=' ')