import test_graph
import functions
from functions import *
exit = True

while exit:
    print("Which graph do you wan to test ? Choose a number between 1 and 13")
    num = int(input())

    # To display the chosen graph
    graph_test = test_graph.graph_test[num - 1]
    print("\nInitial graph :")
    display_table(graph_test)
    print("\n")
    # To display the resulted graph
    result = floyd_warshall(test_graph.graph_test[num - 1])
    print("\n\nFloyd Warshall graph", end=' ')
    display_table(result)

    # Here we need to say if there is an absorbent cycle or not

    print("\nDo you want to test another graph ? (Yes or No)")
    question = input()

    if question == "No":
        exit = False

