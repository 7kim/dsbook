def create_edges(graph):                  #function to create edges between nodes and neighbors.

    edges = []                              # an empty list of edges.
    for key in graph:                              # for each key or node in mygraph
        for value in graph[key]:                              #for each value or neighbor in key or node.
            edges.append((key, value))                              #append key and value for each neighbor in a node.

    return edges                              #get me my edges back

def generate_isolated(graph):
     isolated = []
     for key in graph:
         if not graph[key]:
             isolated+=key #node
     return isolated



graph = { "a" : ["c"],"b" : ["c", "e"],"c" : ["a", "b", "d", "e"],"d" : ["c"],"e" : ["c", "b"],"f" : [] ,"G" : [],"H" : []}
print(create_edges(graph))
print("the isolated nodes are : ",generate_isolated(graph))