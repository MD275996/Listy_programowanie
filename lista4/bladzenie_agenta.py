#będziemy używali networkx
#strona pomocnicza https://networkx.org/documentation/stable/tutorial.html

import networkx as nx
import matplotlib.pyplot as plt

def random_graph(n,p):
    G = nx.Graph()                                              #stwarzamy graf
    G.add_nodes_from(range(n))
    print(G.number_of_nodes)

    ax = plt.subplot()
    nx.draw(G, with_labels=True, font_weight = 'bold')
    plt.show()

random_graph(7,0.5)