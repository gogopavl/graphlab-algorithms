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

sssp = gl.shortest_path.create(g, source_vid=0)

result = sssp.get_path(vid=10001)

print result

tic = time.time()

print("Total runtime: {} seconds".format(tic-toc))