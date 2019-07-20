# GraphLab Algorithms

Repository containing various graph algorithm implementations using GraphLab.

## Installation

To install GraphLab follow steps as shown in [installation guide](https://turi.com/download/install-graphlab-create.html).

## Running

Activate the conda environment and run any of the python scripts.

### Activating the Virtual Environment
```
source activate gl-env
```

### Running the Algorithms 

- pagerank, connected-components, triangle-counting
    ```
    python script.py W /path/to/edgelist
    ```
    * where W is the number of workers (cores)
    * e.g. `python pagerank.py 8 ~/data/soc-LiveJournal1.txt` (to execute on 8 cores)

- single-source-shortest-path, reachability (sp version)
    ```
    python script.py W /path/to/edgelist S T
    ```
    * where S the source vertex id and T the target vertex id
    * the DFS and BFS implementations of reachability also receive an additional argument M (max_depth) to limit the search depth

- neighbors
    ```
    python neighbors.py W /path/to/edgelist S D
    ```
    * where S the source vertex id and D the neighborhood degree

## SW Versions

- Python 2.7.1
- Anaconda 4.3.30
- pip 9.0.1 (Do not upgrade to latest, otherwise you might be facing [this error](https://stackoverflow.com/questions/50129762/graphlab-create-2-1-installation-fails-to-uninstall-certifi-a-distutils-insta))

## License

As stated in [LICENSE](https://github.com/pgogousis/graph-lab-algorithms/blob/master/LICENSE).