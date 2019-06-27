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

tri = gl.triangle_counting.create(g)

tic = time.time()

print tri.summary()

tri_out = tri['triangle_count']
print tri_out.topk('triangle_count', k=10) # Printing top 10 nodes based on their triangle count

print("Total runtime: {} seconds".format(tic-toc))