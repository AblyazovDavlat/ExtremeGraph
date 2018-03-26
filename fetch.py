import networkx as nx
from networkx.algorithms import isomorphism

def euler_cycle (graph):
    if (nx.is_eulerian(graph)):
       return list(nx.eulerian_circuit(graph))
    else:
       return (False)

def is_line_graph (graph, G1, G2, G3, G4, G5, G6, G7, G8, G9):
    GM1 = isomorphism.GraphMatcher(graph,G1)
    GM2 = isomorphism.GraphMatcher(graph,G2)
    GM3 = isomorphism.GraphMatcher(graph,G3)
    GM4 = isomorphism.GraphMatcher(graph,G4)
    GM5 = isomorphism.GraphMatcher(graph,G5)
    GM6 = isomorphism.GraphMatcher(graph,G6)
    GM7 = isomorphism.GraphMatcher(graph,G7)
    GM8 = isomorphism.GraphMatcher(graph,G8)
    GM9 = isomorphism.GraphMatcher(graph,G9)

    if (GM1.subgraph_is_isomorphic() or GM2.subgraph_is_isomorphic() or GM3.subgraph_is_isomorphic() or
            GM4.subgraph_is_isomorphic() or GM5.subgraph_is_isomorphic() or GM6.subgraph_is_isomorphic() or
            GM7.subgraph_is_isomorphic() or GM8.subgraph_is_isomorphic() or GM9.subgraph_is_isomorphic()):
        return False

    return True

def is_dirak_graph (graph):
    degree = graph.degree(1)
    if (len(graph)>2):
        for node in nx.nodes(graph):
            if (graph.degree(node)) < degree:
                degree = graph.degree(node)
    if (degree < len(graph)/2):
        return False
    return True

def hamilton_cycle (graph):
    startVertex = list(nx.nodes(graph))[0]  #стартовая вершина
    N = list()                              #список вершин смежных с текущей вершиной
                                            #ребро между которыми еще не рассматривалось
    cycle = list()                          #текущий список вершин в цикле
    cycle.append(startVertex)

    for line in nx.generate_adjlist(graph): #генерирум список смежных вершин
        N.append(list(line.replace(' ','')))

    while (len(cycle)!=0):
        x = cycle.pop()                     #
        cycle.append(x)                     # top()
        if (len(N[x])!= 0):
            y = N[x].pop()
            if (not(y in cycle)):
                cycle.append(y)
                if (len(cycle) == nx.number_of_nodes(graph)):
                    if(startVertex in N[cycle.pop()]):
                        return cycle
                    elif (len(cycle) == nx.number_of_nodes(graph)):
                        cycle.pop()
        else:
            cycle.pop()
    return False






