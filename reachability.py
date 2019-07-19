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

    graph = gl.load_graph(path, 'snap')

    sources_set = set([source_vertex]) # Start from source vertex - BFS
    targets_set = set()

    is_reachable = False

    while max_depth > 0:
        for vertex in sources_set:
            outgoing_edges = graph.get_edges(src_ids=[vertex])
            targets_set.update(list(outgoing_edges["__dst_id"]))
        
        if target_vertex in targets_set:
            is_reachable = True
            break
        else:
            sources_set = targets_set
            targets_set = set()
        max_depth -= 1

    tic = time.time()

    if is_reachable:
        print("Vertex {} is reachable from vertex {}".format(target_vertex, source_vertex))
    else:
        print("Vertex {} cannot be reached from vertex {}".format(target_vertex, source_vertex))

    return "Total runtime: {} seconds".format(tic-toc)

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