import graphlab as gl
import time
import sys

# Neighborhood list
neighbors = set()

def run_ndegree_neigh_job (path_to_file, source_vertex, degree):
    """Finds the nth degree neighborhood on the specified graph using graphlab's API.
    Parameters
    ----------
    path_to_file : String type
        The path leading to the edge list file
    source_vertex : Long type
        The id of the source vertex
    
    degree : int type
        The degree of neighbors
    Returns
    -------
    runtime : String type
        The total runtime of the job
    """
    
    toc = time.time()

    g = gl.load_graph(path, 'snap')

    result = nth_neighborhood(g, source_vertex, degree)
    print("Neighorhood length: {}\nNeighbors:\n{}".format(len(neighbors), neighbors))

    tic = time.time()

    return "Total runtime: {} seconds".format(tic-toc)

def nth_neighborhood(graph, source_vertex, degree):
    """Recursive helper method used to traverse graph.
    Parameters
    ----------
    graph : Graph type
        The graph used
    
    source_vertex : Long type
        The id of the source vertex
    
    degree : int type
        The degree of neighbors
    """
    global neighbors

    outgoing_edges = graph.get_edges(src_ids=[source_vertex])
    neighborhood_ids = outgoing_edges["__dst_id"]

    if degree is 1:
        neighbors.update(list(neighborhood_ids))
        return
    else:
        for vertex in neighborhood_ids:
            nth_neighborhood(graph, vertex, degree-1)
    return True

if __name__ == '__main__':

    if(len(sys.argv) is 1):
        print("Please add number of workers, dataset path, source vertex, and neighborhood degree as arguments when loading script")
        sys.exit()
    else:
        workers = int(sys.argv[1])
        path = sys.argv[2]
        source_vertex = long(sys.argv[3])
        degree = int(sys.argv[4])
    
    # Configure GraphLab to utilize a specific number of workers (cores)
    gl.set_runtime_config('GRAPHLAB_DEFAULT_NUM_PYLAMBDA_WORKERS', workers)

    ndegree_job = gl.deploy.job.create(run_ndegree_neigh_job, path_to_file=path, source_vertex=source_vertex, degree=degree)

    # Collect job status, result, and metrics
    print("Job status\n{}".format(ndegree_job.get_status())) 
    print("Job results\n{}".format(ndegree_job.get_results())) 
    print("Job metrics\n{}".format(ndegree_job.get_metrics()))