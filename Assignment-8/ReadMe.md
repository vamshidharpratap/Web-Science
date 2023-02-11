# Herding and Preferential Attachment

Consider the following (rather simple) generative model for the Web, where a webpage can be seen as a node, and a hyperlink between two webpages can be seen as a link.

It starts with a single node at timestep t=1. The node has one link to itself,meaning it has degree k = 2 (one indegree and one outdegree);
At each timestep t> 1, a new node (without a self-loop) joins the Web, and creates a link to one of the existing nodes.

Consider the two situations. For each t> 1, the new node creates its outgoing link to an existing node:

1. with equal probability;
2. with probability p(i) proportional to the degree of the existing node k(1)

# 2.1 Simulation 

Write a program to simulate this generative model for both situations, and plot the degree distribution at t 10000. What axis scales do you use for each situation? Why?

# 2.2 Entropy

Write your own function to calculate the entropy of a (discrete) probability distribution (with base 2), and apply it to both degree distributions in the previous task

# 2.3 Analytical Solution

Please analytically give the degree distribution for both situations at t→ +∞.

