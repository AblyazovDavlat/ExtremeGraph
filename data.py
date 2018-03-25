import networkx as nx

def create_G1():
    G = nx.complete_bipartite_graph(1,3)
    return G

def create_G2():
    G = nx.cycle_graph(5)
    G.add_edge(2,4)
    G.add_edge(3,5)
    return G

def create_G3():
    G = create_G2()
    G.add_edge(1,3)
    G.add_edge(1,4)
    return G

def create_G4():
    G = nx.Graph()
    G.add_nodes_from([1,6])
    G.add_edges_from([(1,2),(2,3),(2,4),(3,4),(3,5),(4,5),(5,6)])
    return G

def create_G5():
    G = create_G4()
    G.add_edge(3,6)
    G.add_edge(4,6)
    return G

def create_G6():
    G = create_G5()
    G.add_edge(1,3)
    G.add_edge(1,4)
    return G

def create_G7():
    G = nx.Graph()
    G.add_nodes_from([1, 6])
    G.add_edges_from([(1, 2), (2, 3), (2, 4), (3, 4), (3, 6), (4, 6), (1, 5),(5, 6)])
    return G

def create_G8():
    G = create_G4()
    G.add_edge(1,3)
    G.add_edge(4,6)
    return G

def create_G9():
    G = nx.cycle_graph(5)
    G.add_node(6)
    G.add_edges_from([(1,6),(2,6),(3,6),(4,6),(5,6)])
    return G