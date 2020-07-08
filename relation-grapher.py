import networkx as nx
import matplotlib.pyplot as plt


def graphRelations(nouns, relationships, semantic):
    graphRelation1(nouns, relationships, semantic)
    graphRelation2(nouns, relationships, semantic)
    return


def graphRelation1(nouns, relationships, semantic):
    # Graph the relationships
    G1 = nx.Graph()
    G1.add_nodes_from(nouns)
    G1.add_nodes_from(semantic[1])
    print('Nodes:')
    print(G1.nodes)
    pos = nx.circular_layout(G1)
    for i in range(0, len(semantic[2])):
        try:
            G1.add_edge(semantic[0], semantic[1][i], name=semantic[2][i])
        except:
            pass

    for i in range(0, len(relationships)):
        try:
            G1.add_edge(nouns[i], nouns[i + 1], name=relationships[i])
        except:
            pass
    labels = nx.get_edge_attributes(G1, 'name')
    nx.draw_networkx(G1, pos=pos, node_size=5000, font_size=10, with_labels=True)
    nx.draw_networkx_edge_labels(G1, pos, edge_color='black', edge_labels=labels)
    plt.show()
    return


def graphRelation2(nouns, relationships, semantic):
    if len(nouns) > 2:
        G1 = nx.Graph()
        G1.add_nodes_from(nouns)
        G1.add_nodes_from(semantic[1])
        pos = nx.circular_layout(G1)
        for i in range(0, len(semantic[2])):
            try:
                G1.add_edge(semantic[0], semantic[1][i], name=semantic[2][i])
            except:
                pass
        for i in range(0, len(relationships)):
            try:
                G1.add_edge(nouns[0], nouns[i + 1], name=relationships[i])
            except:
                pass
        labels = nx.get_edge_attributes(G1, 'name')
        nx.draw_networkx(G1, pos=pos, node_size=5000, font_size=10, with_labels=True)
        nx.draw_networkx_edge_labels(G1, pos, edge_color='black', edge_labels=labels)
        plt.show()
    return