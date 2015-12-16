from igraph import *
import time

# Let's look at graph creation tricks...

# We create a list with vertices
mylist = list(xrange(100000))

# Now, let's compare time to add vertices to graphs
g1 = Graph()
g2 = Graph()

# Adding vertices one by one...
start_time = time.time()
for i in mylist:
    g1.add_vertex(id=i)
end_time = time.time()

print("\n--- Nodes added one by one in  %s seconds" % (end_time - start_time))

# Adding vertices all together...
start_time = time.time()
g2.add_vertices(100000)
end_time = time.time()

print("\n--- Nodes added in  %s seconds" % (end_time - start_time))
