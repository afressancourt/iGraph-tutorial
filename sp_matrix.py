import time
from igraph import *

# We build shortest paths matrix ...

# Erdos Renyi undirected graph...
g_und = Graph.Erdos_Renyi(4000, 0.05, directed=False, loops=False)
print summary(g_und)

# We build the shortest paths matrix for the graph...
start_time = time.time()
shortest_matrix = g_und.shortest_paths()
end_time = time.time()
print("\n--- SP matrix found in  %s seconds ---" % (end_time - start_time))

source = []
destination = []
for i in range(1000):
    source += [i]
    destination += [i+1000]

# We try to find shortests paths for 1000 sources in
# the Erdos Renyi undirected graph
start_time = time.time()
shortest_matrix_2 = g_und.shortest_paths(source=source)
end_time = time.time()
print("\n--- SP matrix found in  %s seconds ---" % (end_time - start_time))

# We try to find shortests paths for 1000 sources and 1000 destinations in
# the Erdos Renyi undirected graph
start_time = time.time()
shortest_matrix_3 = g_und.shortest_paths(source=source,
                                         target=destination)
end_time = time.time()
print("\n--- SP matrix found in  %s seconds ---" % (end_time - start_time))
