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

# Source and destination vertices
source_vertex_id = 1004
destination_vertex_id = 3655
max_depth = 2

assert max_depth >= 1

def is_reachable(graph, source_vertex, destination_vertex, max_depth):
    
    outgoing_edges = graph.get_edges(src_ids=[source_vertex])
    neighborhood_ids = outgoing_edges["__dst_id"]

    if destination_vertex in neighborhood_ids:
        return True
    else:
        if (max_depth > 1):
            for vertex in neighborhood_ids:
                if (is_reachable(graph.get_neighborhood(ids=[vertex]), vertex, destination_vertex, max_depth-1)):
                    return True
    return False


result = is_reachable(g, source_vertex_id, destination_vertex_id, max_depth)    

tic = time.time()

if result:
    print("Vertex {} is reachable from vertex {}".format(destination_vertex_id, source_vertex_id))
else:
    print("Vertex {} cannot be reached from vertex {}".format(destination_vertex_id, source_vertex_id))

print("Total runtime: {} seconds".format(tic-toc))