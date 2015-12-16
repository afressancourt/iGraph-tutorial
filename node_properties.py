import random
from igraph import *

# Let's give properties to nodes...

graph = Graph()

# We add 100000 nodes to the graph...
graph.add_vertices(100000)

# We add a name to each node....
for element in graph.vs:
    el_name = "Node " + str(element.index)
    element["name"] = el_name

# Now let's add some edges

edges_list = []
for element in graph.vs:
    source = element.index
    for i in range(30):
        target = random.randint(0, 99999)
        edges_list += [(source, target)]

graph.add_edges(edges_list)

for element in graph.es:
    element["type"] = random.randint(0, 3)

print summary(graph)
