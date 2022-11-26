import networkx as nx
import matplotlib.pyplot as plt
from sys import argv

class Link:                                         # Defining the Disjoint Set Union data structure 
    def __init__(self, first,second,cost):
        self.u=first
        self.v=second
        self.cost=cost


def findPar(u,parent):
    if u==parent[u]:
        return u
    return findPar(parent[u],parent)

def unionn(u,v,parent,rank):
    u = findPar(u, parent)
    v = findPar(v, parent)

    if rank[u] < rank[v]:
        parent[u] = v
    elif rank[v] < rank[u]:
        parent[v] = u
    else:
        parent[v] = u
        rank[u] = rank[u]+1  



def takeNetworkInput(links) :
    input_file = open(argv[1],'r')
    Line = input_file.readline()
    Line = Line.strip().split(' ')

    num_nodes= int(Line[0])

    num_links = int(Line[1])

    for i in range(num_links) :
        line = input_file.readline()
        line = line.strip().split(' ')
        u = int(line[0])
        v = int(line[1])
        cost = int(line[2])
        links.append(Link(u,v,cost))

    links.sort(key  = lambda x: x.cost)

    for link in links:
        print(link.u,' -> ',link.v,' link cost: ',link.cost)
    print()
    
    return num_nodes, num_links

def visualize(links):
    G = nx.Graph()
    for router_links in links:
        G.add_edge(router_links.u,router_links.v,weight=router_links.cost)

         
    pos = nx.spring_layout(G, seed=7)  

            # nodes
    nx.draw_networkx_nodes(G, pos, node_size=700)

    # routers
    nx.draw_networkx_edges(G, pos)
            
    # router labels
    nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")
    # link weight labels
    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels)

    plt.title("Network")
    plt.show()        


def visualizeMST(mst):
            G = nx.Graph()
            for router_links in mst:
                G.add_edge(router_links[0],router_links[1],weight=router_links[2])

         
            pos = nx.spring_layout(G, seed=7)  # positions for all nodes - seed for reproducibility

            # nodes
            nx.draw_networkx_nodes(G, pos, node_size=700)

            # edges
            nx.draw_networkx_edges(G, pos)
            
            # node labels
            nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")
            # edge weight labels
            edge_labels = nx.get_edge_attributes(G, "weight")
            nx.draw_networkx_edge_labels(G, pos, edge_labels)


            plt.title("Minimum Spanning Tree (MST)")
            plt.show()

def kruskal(links, parent, mst, rank, costt):

    for link in links:
        if findPar(link.v, parent) != findPar(link.u, parent) :
            costt += link.cost
            mst.append((link.u,link.v,link.cost))
            unionn(link.u,link.v,parent,rank)

    for link in mst:
        print(link[0],' ',link[1],' ',link[2])

    return costt