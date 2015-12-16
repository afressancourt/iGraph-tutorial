from igraph import *
import time

# Let's look at graph creation tricks...

# We create a list with vertices
mylist = list(xrange(100))
# We will connect every vertice to every single other
crosspairs = [(a, b) for a in mylist for b in mylist if a != b]

# Now, let's compare time to add vertices to graphs
g1 = Graph()
g2 = Graph()

# Adding vertices all together...
g1.add_vertices(100)
g2.add_vertices(100)

# Adding edges one by one...
start_time = time.time()
for element in crosspairs:
    g1.add_edge(element[0], element[1])
end_time = time.time()

print("\n--- Edges added one by one in  %s seconds" % (end_time - start_time))

# Adding edges all together...
start_time = time.time()

g2.add_edges(crosspairs)

end_time = time.time()

print("\n--- Edges added together in  %s seconds" % (end_time - start_time))
