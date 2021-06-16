import networkx as nx
import matplotlib.pyplot as plt


Graph = nx.petersen_graph()
nx.draw_shell(Graph, nlist=[range(5, 10), range(5)])
plt.show()

H = nx.path_graph(10)
nx.draw(H)
plt.show()

I = nx.star_graph(7)
nx.draw(I)
plt.show()

J = nx.wheel_graph(5)
nx.draw(J)
plt.show()