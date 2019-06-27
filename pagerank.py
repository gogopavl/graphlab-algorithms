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

pr = gl.pagerank.create(g, max_iterations=20)

tic = time.time()

print pr.summary()

pr_out = pr['pagerank']

print pr_out.topk('pagerank', k=10) # Printing top 10 nodes based on their PR

print("Total runtime: {} seconds".format(tic-toc))