import graphlab as gl
import time
import sys

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

    graph = gl.load_graph(path, 'snap')

    sources_set = set([source_vertex]) # Start from source vertex - BFS
    targets_set = set()

    while degree > 0:
        for vertex in sources_set:
            outgoing_edges = graph.get_edges(src_ids=[vertex])
            targets_set.update(list(outgoing_edges["__dst_id"]))
        
        if degree is 1:
            nth_neighbors = targets_set
            break
        else:
            sources_set = targets_set
            targets_set = set()
        degree -= 1
        

    print("Neighorhood length: {}\nNeighbors:\n{}".format(len(nth_neighbors), nth_neighbors))

    tic = time.time()

    return "Total runtime: {} seconds".format(tic-toc)

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