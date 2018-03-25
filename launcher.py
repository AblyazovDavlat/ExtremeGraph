import networkx as nx
import fetch
import data

G1 = data.create_G1()
G2 = data.create_G2()
G3 = data.create_G3()
G4 = data.create_G4()
G5 = data.create_G5()
G6 = data.create_G6()
G7 = data.create_G7()
G8 = data.create_G8()
G9 = data.create_G9()
graph = nx.cycle_graph(4)
graph.add_node(4)
graph.add_edge(0,4)
graph.add_edge(3,4)

def hamilton_cycle (graph):
    if (fetch.is_line_graph(graph, G1, G2, G3, G4, G5, G6, G7, G8, G9)):
        line_graph = nx.line_graph(graph)
        euler = fetch.euler_cycle(line_graph)
        if (euler != False):
            return list(euler)
        return euler
    return (fetch.is_line_graph(graph, G1, G2, G3, G4, G5, G6, G7, G8, G9))

print(list(graph))
print(list(nx.line_graph(graph)))