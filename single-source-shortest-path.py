import graphlab as gl
import time
import sys

def run_sssp_job (path_to_file, source_vertex, target_vertex):
    """Finds the shortest path from a given vertex to a target vertex on the specified graph using graphlab's API.

    Parameters
    ----------
    path_to_file : String type
        The path leading to the edge list file

    source_vertex : Long type
        The id of the source vertex

    target_vertex : Long type
        The id of the target vertex

    Returns
    -------
    runtime : String type
        The total runtime of the job
    """
    
    toc = time.time()

    g = gl.load_graph(path, 'snap')

    sssp = gl.shortest_path.create(g, source_vid=source_vertex)

    result = sssp.get_path(vid=target_vertex)

    print result

    tic = time.time()

    return "Total runtime: {} seconds".format(tic-toc)

if __name__ == '__main__':

    if(len(sys.argv) is 1):
        print("Please add number of workers, dataset path, source vertex and target vertex as arguments when loading script")
        sys.exit()
    else:
        workers = int(sys.argv[1])
        path = sys.argv[2]
        source_vertex = long(sys.argv[3])
        target_vertex = long(sys.argv[4])
    
    # Configure GraphLab to utilize a specific number of workers (cores)
    gl.set_runtime_config('GRAPHLAB_DEFAULT_NUM_PYLAMBDA_WORKERS', workers)

    sssp_job = gl.deploy.job.create(run_sssp_job, path_to_file = path, source_vertex=source_vertex, target_vertex=target_vertex)

    # Collect job status, result, and metrics
    print("Job status\n{}".format(sssp_job.get_status())) 
    print("Job results\n{}".format(sssp_job.get_results())) 
    print("Job metrics\n{}".format(sssp_job.get_metrics())) 