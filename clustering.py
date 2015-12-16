from igraph import *
import time
import fix_clustering

# A look at clustering in iGraph...
graph = Graph.Erdos_Renyi(2000, 0.01)

print "\n# Classical Clustering:"
start_time = time.time()
clusters = graph.clusters()
end_time = time.time()
sec = end_time - start_time
print("--- Clustering found %s clusters ---" % len(clusters))

print "\n# Fast Greedy Clustering:"
dendrogram = graph.community_fastgreedy()
clusters = dendrogram.as_clustering()
print("---Fast Greedy Clustering found %s clusters ---" % len(clusters))

print "\n# Walktrap Clustering:"
dendrogram = graph.community_walktrap()
try:
    clusters = dendrogram.as_clustering()
except InternalError:
    fix_clustering.fix_dendrogram(graph, dendrogram)
    clusters = dendrogram.as_clustering()
print("---Walktrap Clustering found %s clusters ---" % len(clusters))
