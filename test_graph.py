import math
Inf = math.inf

# Enter the relation table of the graph,
# For example, set a 0 when it's a relation with the same relation of 1 with 1 is none, so 0 here
# And put Inf when the relation doesn't exits between twoo (no relation between 1 and 2 ? so put Inf)

graph_test = [   [[0, 1, 5, Inf], # test graph 1
                 [Inf, 0, -3, 5],
                 [Inf, Inf, 0, 2],
                 [Inf, Inf, Inf, 0]],

                [[0, 1, 4, Inf, Inf], # test graph from website
                 [Inf, 0, 2, Inf, Inf],
                 [Inf, Inf, 0, 3, 8],
                 [6, Inf, Inf, 0, 4],
                 [5, Inf, Inf, Inf, 0]],

                [[0, 1, -5, Inf], # test graph 3
                 [Inf, 0, -3, 2],
                 [Inf, 4, 0, 2],
                 [Inf, Inf, Inf, 0]]
            ]


