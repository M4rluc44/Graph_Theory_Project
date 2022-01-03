import math
Inf = math.inf

# Enter the relation table of the graph,
# For example, set a 0 when it's a relation with the same relation of 1 with 1 is none, so None here

graph_test = [   [[None, 1, 5, None], # test graph 1
                 [None, None, -3, 5],
                 [None, None, None, 2],
                 [None, None, None, None]],

                [[None, 1, 5, None], # test graph 2
                 [None, None, 3, 5],
                 [None, None, None, 2],
                 [None, None, None, None]],

                [[None, 1, -5, None], # test graph 3
                 [None, None, -3, 2],
                 [None, 4, None, 2],
                 [None, None, None, None]],

                [[None, 1, -5, None], # test graph 4
                 [None, None, -3, 2],
                 [6, 4, None, 2],
                 [None, None, 2, None]],

                [[None, 1, -5, None], # test graph 5
                 [None, -1, -3, 2],
                 [6, 4, None, 2],
                 [None, None, 2, None]],

                [[None, 2, -5, None, None, None, None], # test graph 6
                 [None, 3, -3, 3, None, None, None],
                 [7, 4, None, 3, None, None, None],
                 [None, None, 2, None, None, None, None],
                 [None, None, None, None, None, 5, None],
                 [None, None, None, None, 2, 0, -2],
                 [None, None, None, None, None, None, None]],

                [[None, 1, 2, 1, None], # test graph 7
                 [None, None, None, None, 3],
                 [None, None, None, 1, 1],
                 [None, None, None, None, 4],
                 [None, None, None, None, None]],

                [[None, 1, None, None, None], # test graph 8
                 [None, None, 2, None, None],
                 [None, None, None, 3, None],
                 [None, None, None, None, -6],
                 [0, None, None, None, None]],

                [[None, 1, -5, None], # test graph 9
                 [None, None, -3, 2],
                 [None, -1, None, 2],
                 [None, None, None, None]],

                [[None, None, 2, 1, None, None, None, None], # test graph 10
                 [1, None, None, None, 1, None, None, None],
                 [None, None, None, -2, None, None, None, None],
                 [None, None, 7, None, 4, None, None, None],
                 [None, 3, -1, None, None, None, None, None],
                 [None, None, None, None, None, 2, None, None],
                 [None, None, None, None, None, -2, None, -2],
                 [None, None, None, None, None, None, None, None]],

                [[None, None, 2, 1, None], # test graph 11
                 [1, 2, None, None, None],
                 [None, None, None, -2, None],
                 [None, None, None, None, 4],
                 [None, 3, -1, None, None]],

                [[None, 1, 2, 1, None], # test graph 12
                 [None, 2, None, None, None],
                 [None, None, None, -2, 1],
                 [None, None, None, None, 4],
                 [None, 3, None, None, None]],

                [[None, None, 2, 1, None, None, None, None], # test graph 13
                 [1, None, None, None, 1, None, None, None],
                 [None, None, None, -2, None, None, None, None],
                 [None, None, 7, None, 4, None, None, None],
                 [None, 3, -1, None, None, None, None, None],
                 [None, None, None, None, None, None, 1, None],
                 [None, None, None, None, None, -2, None, -2],
                 [None, None, None, None, None, None, None, None]]

            ]


