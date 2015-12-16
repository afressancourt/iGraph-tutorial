from igraph import *

# Your first graph with iGraph !

g = Graph()

print summary(g)

# Let's add vertices...

g.add_vertices(15)

print summary(g)

# Now let's add edges one by one...
g.add_edge(2, 0)
g.add_edge(2, 3)

print summary(g)

# ... or in batch...
g.add_edges([(2, 13),
             (3, 4),
             (13, 14),
             (4, 5),
             (5, 3)])

print summary(g)

# We can get information on the graph...
# Degree...
print g.degree()

# Diameter...
print g.diameter()
