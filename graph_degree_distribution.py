#using NetworkX
import matplotlib.pyplot as plt

# Compute the degree of every node in the graph: 
# So degrees is the degree distribution of this graph 
degrees = [len(T.neighbors(n)) for n in T.nodes()]

# Compute the degree centrality of the Twitter network: deg_cent
deg_cent = nx.degree_centrality(T)

# Plot a histogram of the degree centrality distribution of the graph.
plt.figure()
plt.hist(list(deg_cent.values()))
plt.show()

# Plot a histogram of the degree distribution of the graph
plt.figure()
plt.hist(degrees)
plt.show()

# Plot a scatter plot of the centrality distribution and the degree distribution
plt.figure()
plt.scatter(degrees, list(deg_cent.values()))
plt.show()

#the graphs show there is perfect correlation between the degree centrality distribution and the degree distribution


