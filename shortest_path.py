import time
from igraph import *
from random import randint

# We show how to find shortest paths ...

# Erdos Renyi undirected graph...
g_und = Graph.Erdos_Renyi(40000, 0.05, directed=False, loops=False)
print summary(g_und)

# Erdos Renyi directed graph...
g_dir = Graph.Erdos_Renyi(40000, 0.05, directed=True, loops=False)
print summary(g_dir)

# We try to find 1000 shortests paths at random in
# the Erdos Renyi undirected graph
und_paths = []
start_time = time.time()
for i in range(1000):
    und_paths += [g_und.get_shortest_paths(randint(1, 399), randint(1, 399))]
end_time = time.time()
print("\n--- Paths found in  %s seconds ---" % (end_time - start_time))

# We try to find 1000 shortests paths at random in
# the Erdos Renyi directed graph
dir_paths = []
start_time = time.time()
for i in range(1000):
    dir_paths += [g_dir.get_shortest_paths(randint(1, 399), randint(1, 399))]
end_time = time.time()
print("\n--- Paths found in  %s seconds ---" % (end_time - start_time))
