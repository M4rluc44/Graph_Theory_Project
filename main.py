import test_graph
import functions

exit = True

while exit:
    print("Which graph do you wan to test ? Choose a number between 1 and 13")
    num = int(input())
    result = functions.floyd_warshall(test_graph.graph_test[num - 1])

    print("\nInitial graph :")
    for i in range(len(test_graph.graph_test[num - 1])):
        print("")
        for j in range(len(test_graph.graph_test[num - 1][i])):
            print(test_graph.graph_test[num - 1][i][j], "|", end=' ')

    print("\nFloyd Warshall graph")
    for i in range(len(result)):
        print("")
        for j in range(len(result[i])):
            print(result[i][j], "|", end=' ')

    print("\nDo you want to test another graph ? (Yes or No)")
    question = input()

    if question == "No":
        exit = False
