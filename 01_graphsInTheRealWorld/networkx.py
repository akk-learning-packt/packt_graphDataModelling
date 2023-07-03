#!/usr/bin/env python3
import networkx as nx
import matplotlib.pyplot as plt

# to create an empty graph, g
g = nx.Graph()

# adding one node at a time
g.add_node("Jeremy")

# alternatively, multiple nodes can be added
g.add_nodes_from(["Mark", "Smith"])

# Properties can be added to nodes during creation by passing a node
# and dictionary tuple
g.add_nodes_from([("Mark", {"followers": 2100}), ("Smith", {"followers": 130})])

# to add an edge to the graph
g.add_edge("Jeremy", "Mark")

# any nodes specified as part of that edge not already in the graph
# will be added implicitly.

# Plot it

nx.draw(g, with_labels=True)
# plt.savefig("./img/intro_graph.png")
plt.show()

x = [1, 2, 3, 4, 5, 6]
y = [2, 4, 1, 2, 3, 5]

fig, ax = plt.subplots()
fig.set_facecolor("w")
ax.plot(x, y)
plt.show()
