import graphlab as gl
import time
import sys

def run_triangle_counting_job (path_to_file):
    """Calculates the number of triangles on the specified graph using graphlab's API.

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

    tri = gl.triangle_counting.create(g)

    tic = time.time()

    print tri.summary()

    tri_out = tri['triangle_count']

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

    tc_job = gl.deploy.job.create(run_triangle_counting_job, path_to_file = path)

    # Collect job status, result, and metrics
    print("Job status\n{}".format(tc_job.get_status())) 
    print("Job results\n{}".format(tc_job.get_results())) 
    print("Job metrics\n{}".format(tc_job.get_metrics())) 