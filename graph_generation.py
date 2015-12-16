from igraph import *

# Now let's generate graph according to a well-known model...

# Barabasi graph...
g_bar = Graph.Barabasi(400,
                       100,
                       outpref=False,
                       directed=False,
                       power=1,
                       zero_appeal=1,
                       implementation="psumtree",
                       start_from=None)
print summary(g_bar)

# Erdos Renyi graph...
g_erd = Graph.Erdos_Renyi(400, 0.9, directed=False, loops=False)
print summary(g_erd)

# Erdos Renyi graph...
g_erd = Graph.Erdos_Renyi(400, 0.9, directed=False, loops=False)
print summary(g_erd)

# Growing random graph...
g_gra = Graph.Growing_Random(400, 1000, directed=False, citation=False)
print summary(g_gra)

# De Bruijn graph...
g_dbr = Graph.De_Bruijn(4, 10)
print summary(g_dbr)
