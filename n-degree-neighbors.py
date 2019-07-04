import graphlab as gl
import time
import sys

if(len(sys.argv) is 1):
    print("Please pass dataset path as an argument when loading script")
    sys.exit()
else:
    path = sys.argv[1]

toc = time.time()

g = gl.load_graph(path, 'snap')

# Degree
degree = 2

assert degree >= 1

# Source vertex
source_vertex_id = 1004

# Neighborhood list
neighbors = list()

def nth_neighborhood(graph, source_vertex, degree):
    global neighbors

    outgoing_edges = graph.get_edges(src_ids=[source_vertex])
    neighborhood_ids = outgoing_edges["__dst_id"]

    if degree is 1:
        neighbors.extend(list(neighborhood_ids))
        return
    else:
        for vertex in neighborhood_ids:
            nth_neighborhood(graph, vertex, degree-1)

nth_neighborhood(g, source_vertex_id, degree)
print(neighbors)

tic = time.time()

print("Total runtime: {} seconds".format(tic-toc))