import graphlab as gl
import time
import sys

def run_ndegree_neigh_job (path_to_file, source_vertex, degree):
    """Finds the nth degree neighborhood on the specified graph using graphlab's API. This case ignores direction.

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

    sssp = gl.shortest_path.create(graph, source_vid=source_vertex)
    
    sp_sframe = sssp['distance'].filter_by(float(degree), 'distance')

    print("Neighorhood length: {}\nNeighbors:\n{}".format(sp_sframe.num_rows(), sp_sframe))

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