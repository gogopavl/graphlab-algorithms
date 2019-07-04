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

conn_comp = gl.connected_components.create(g)

tic = time.time()

print conn_comp.summary()

print("Total runtime: {} seconds".format(tic-toc))