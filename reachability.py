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
destination_vertex_id = 1007

def has_neighbor(graph, source_vertex, destination_vertex):
    
    outgoing_edges = graph.get_edges(src_ids=[source_vertex])
    neighborhood_ids = outgoing_edges["__dst_id"]

    if destination_vertex in neighborhood_ids:
        return True
    else:
        for vertex in neighborhood_ids:
            has_neighbor(graph.get_neighborhood(ids=[vertex]), vertex, destination_vertex)
    return False


is_reachable = has_neighbor(g, source_vertex_id, destination_vertex_id)    

tic = time.time()

if is_reachable:
    print("Vertex {} is reachable from vertex {}".format(destination_vertex_id, source_vertex_id))
else:
    print("Vertex {} cannot be reached from vertex {}".format(destination_vertex_id, source_vertex_id))

print("Total runtime: {} seconds".format(tic-toc))