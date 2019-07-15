import graphlab as gl
import time
import sys

def run_reachability_job (path_to_file, source_vertex, target_vertex, max_depth):
    """Determines whether a target vertex is reachable from a source vertex on the specified graph using graphlab's API.

    Parameters
    ----------
    path_to_file : String type
        The path leading to the edge list file

    source_vertex : Long type
        The id of the source vertex
    
    target_vertex : Long type
        The id of the target vertex
    
    max_depth : int type
        The maximum recursion depth

    Returns
    -------
    runtime : String type
        The total runtime of the job
    """
    
    toc = time.time()

    g = gl.load_graph(path, 'snap')

    result = is_reachable(g, source_vertex, target_vertex, max_depth)    

    tic = time.time()

    if result:
        print("Vertex {} is reachable from vertex {}".format(source_vertex, target_vertex))
    else:
        print("Vertex {} cannot be reached from vertex {}".format(source_vertex, target_vertex))

    return "Total runtime: {} seconds".format(tic-toc)

def is_reachable(graph, source_vertex, destination_vertex, max_depth):
    """Recursive helper method used to traverse graph.

    Parameters
    ----------
    graph : Graph type
        The graph used
    
    source_vertex : Long type
        The id of the source vertex
    
    target_vertex : Long type
        The id of the target vertex
    
    max_depth : int type
        The maximum recursion depth

    Returns
    -------
    is_reachable : Boolean type
        True if the target vertex is reachable from the source vertex, otherwise false
    """
    
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

if __name__ == '__main__':

    if(len(sys.argv) is 1):
        print("Please add number of workers, dataset path, source vertex, target vertex, and max recursion depth as arguments when loading script")
        sys.exit()
    else:
        workers = int(sys.argv[1])
        path = sys.argv[2]
        source_vertex = long(sys.argv[3])
        target_vertex = long(sys.argv[4])
        max_depth = int(sys.argv[5])
        assert max_depth >= 1
    
    # Configure GraphLab to utilize a specific number of workers (cores)
    gl.set_runtime_config('GRAPHLAB_DEFAULT_NUM_PYLAMBDA_WORKERS', workers)

    r_job = gl.deploy.job.create(run_reachability_job, path_to_file = path, source_vertex=source_vertex, target_vertex=target_vertex, max_depth=max_depth)

    # Collect job status, result, and metrics
    print("Job status\n{}".format(r_job.get_status())) 
    print("Job results\n{}".format(r_job.get_results())) 
    print("Job metrics\n{}".format(r_job.get_metrics())) 