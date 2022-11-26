import prims
import kruskal

selection = int(input("Please choose the algorithm: \n 1 : Prim's Algorithm \n 2 : Kruskal's Algorithm \n >>  "))

if selection==1 :
    network = {}    
    # Network is stored in a dictonary where key is the source router and each elements in the value list are the destination router
    
    router_count=0   # stores the number of routers in the network
    link_count=0    # stores the number of links in the network
    
    network, router_count, link_count = prims.takeNetworkInput(network, router_count, link_count)
    
    
    prims.visualize(network) # Visulaize the MST of the network
    
    parent = [None]*router_count    # Used to store the parent of router
    key = [1000000]*router_count    # Used to store the link cost between the router and its parent
    mstSet = [False]*router_count   # Used to check is the router has been included into MST or not
    
    prims.prims(network, router_count, parent, key, mstSet) # Runs the Prim's Algorithm and stores the results into parent and key lists

    prims.visulaizeMST(parent, key, router_count)   # Visulaize the MST of the network


  

elif selection == 2:

    num_nodes=0   # stores the number of routers in the network
    num_links=0   # stores the number of links in the network
    links=[]    # Used to store the links in the network

    num_nodes, num_links = kruskal.takeNetworkInput(links) # Taking input

    kruskal.visualize(links)

    parent = [i for i in range(num_nodes)]  
    rank = [0]*num_nodes
    cost=0

    mst = []

    cost = kruskal.kruskal(links, parent, mst, rank,cost)

    kruskal.visualizeMST(mst)
    