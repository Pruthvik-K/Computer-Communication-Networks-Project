import heapq
from sys import argv
import matplotlib.pyplot as plt
import networkx as nx


def takeNetworkInput(network, router_count, link_count) :
  input_file = open(argv[1],'r')  # Opening the file which contains the network information
  Line = input_file.readline()
  Line = Line.strip().split(' ')

  router_count = int(Line[0]) # Total number of routers
  link_count = int(Line[1]) # Total number of links between routers


  for router in range(router_count):
    add_router(router, network, router_count)   # adding routers to the network


  links=[]
  for i in range(link_count) :
    line = input_file.readline()  # reading the links in the network line by line
    line = line.strip().split(' ')

    # Adding the links to the network by considering the router IDs and link cost 
    add_link(int(line[0]),int(line[1]),int(line[2]),network) 

  print_network(network)
  return  network, router_count, link_count
  




# Add a Router to the dictionary
def add_router(v,network,router_count):
  if v in network:
    print("Router ", v, " already exists.")
  else:
    router_count = router_count + 1
    network[v] = []

# Add an link between router u and v with link cost e
def add_link(v1, v2, e,network):
  # Check if router u is a valid router
  if v1 not in network:
    print("Router ", v1, " does not exist.")
  # Check if router v is a valid router
  elif v2 not in network:
    print("Router ", v2, " does not exist.")
  else:
    temp = [v2, e]
    network[v1].append(temp)


# Print the network
def print_network(network):
  print("The network ")
  for vertex in network:
    for edges in network[vertex]:
      print(vertex, " -> ", edges[0], " link cost: ", edges[1])


def visualize(network):
            G = nx.Graph()
            for router_links in network:
                for dest in network[router_links]:
                     G.add_edge(router_links,dest[0],weight=dest[1])

         
            pos = nx.spring_layout(G, seed=7)  # positions for all nodes - seed for reproducibility

            # routers
            nx.draw_networkx_nodes(G, pos, node_size=700)

            # links
            nx.draw_networkx_edges(G, pos)
            
            # router labels
            nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")
            
            # link cost labels
            edge_labels = nx.get_edge_attributes(G, "weight")
            nx.draw_networkx_edge_labels(G, pos, edge_labels)

            plt.title("Network")
            plt.show()
            
        
def visulaizeMST(parent,key,router_count): 
            G = nx.Graph()
            for i in range(1,router_count):
                G.add_edge(parent[i],i,weight=key[i])
                    
            
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


def prims(network,router_count, parent, key ,mstSet):
  key[0]=0
  parent[0]=-1

  pq = []
  heapq.heapify(pq) # converting the list pq to a priority queue
  # A priority queue by default stores the entry with least priority at the front of the queue 

  heapq.heappush(pq,[0,0])

  for i in range(router_count-1):
      u = pq[0][1]
      heapq.heappop(pq)

      mstSet[u]=True

      for link in network[u]:
          v = link[0]
          cost = link[1]
          
          if (mstSet[v] == False) and (cost < key[v]):
              parent[v] = u
              key[v] = cost 
              heapq.heappush(pq,[key[v],v])

