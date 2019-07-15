import graphlab as gl
import time
import sys

def run_conn_comp_job (path_to_file):
    """Finds the connected components on the specified graph using graphlab's API.

    Parameters
    ----------
    path_to_file : String type
        The path leading to the edge list file

    Returns
    -------
    runtime : String type
        The total runtime of the job
    """
    
    toc = time.time()

    g = gl.load_graph(path, 'snap')

    conn_comp = gl.connected_components.create(g)

    tic = time.time()

    print conn_comp.summary()

    return "Total runtime: {} seconds".format(tic-toc)

if __name__ == '__main__':

    if(len(sys.argv) is 1):
        print("Please add number of workers and dataset path as arguments when loading script")
        sys.exit()
    else:
        workers = int(sys.argv[1])
        path = sys.argv[2]

    # Configure GraphLab to utilize a specific number of workers (cores)
    gl.set_runtime_config('GRAPHLAB_DEFAULT_NUM_PYLAMBDA_WORKERS', workers)

    cc_job = gl.deploy.job.create(run_conn_comp_job, path_to_file = path)

    # Collect job status, result, and metrics
    print("Job status\n{}".format(cc_job.get_status())) 
    print("Job results\n{}".format(cc_job.get_results())) 
    print("Job metrics\n{}".format(cc_job.get_metrics()))
