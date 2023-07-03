#!/usr/bin/env python3
import igraph as ig
import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("qtagg")
ig.config["plotting.backend"] = "matplotlib"

g = ig.Graph()

# all nodes have a prescribed internal integer ID.
# The first node that's added has an id of 0, with
# all subsequent nodes assigned increasing integer IDs.

# to add nodes
g.add_vertices(2)

# assign properties
g.vs[0]["name"] = "Jeremy"
g.vs[1]["name"] = "Mark"
g.vs[0]["followers"] = 130
g.vs[1]["followers"] = 2100

# add and edge
g.add_edges([(0, 1)])

# get the summary of its nodes and edges
print(g)

# PLot, cairo
layout = g.layout("kk")
ig.plot(g, layout=layout)

# matplotlib
g.vs["label"] = g.vs["name"]
fig, ax = plt.subplots()
ig.plot(g, layout=layout, target=ax)
plt.show()
