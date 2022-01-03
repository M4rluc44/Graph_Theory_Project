import test_graph
import functions
from functions import *
exit = True
num = 1
while exit:

    #print("Which graph do you wan to test ? Choose a number between 1 and 13")
    #num = int(input())

    # To display the chosen graph
    graph_test = test_graph.graph_test[num - 1]
    print("\nGraph number ", num, "\n")
    print("\nInitial graph :")
    display_table(test_graph.graph_test[num - 1])

    # Here we say if there is an absorbent cycle or not
    # If yes then you have to choose another graph, otherwise it does the floyd_warshall algo
    # To display the resulted graph

    result = floyd_warshall(test_graph.graph_test[num - 1])
    if not result:
        print("\nThere is an absorbent cycle")
    else:
        '''
        u = int(input("\nEnter the initial vertex of the shortest path you want to find"))
        if u<0 or u>len(result):
            print("wrong entry, please enter an integer between 0 and the number of vertex")
            u = int(input("\nEnter the initial vertex of the shortest path you want to find"))
        v = int(input("\nEnter the final vertex of the shortest path you want to find"))
        if u < 0 or u > len(result) or v == u:
            print("wrong entry, please enter an integer between 0 and the number of vertex")
            v = int(input("\nEnter the final vertex of the shortest path you want to find"))
            
        display_path(result, v, u)
        '''
    num += 1
    if num ==14:
        exit = False

    #print("\nDo you want to test another graph ? (Yes or No)")
    #question = input()

    #if question == "No":
    #    exit = False

