class ListRepresentationUndirected:

    def __init__(self):
        self.graph = {}
    
    def add_node(self, v):
        if v in self.graph:
            print(v, 'is already present in the graph')
        else:
           self.graph[v] = []
    
    def add_edge(self, v1, v2):
        if v1 not in self.graph:
             print(v1, 'is not present in the graph')
        elif v2 not in self.graph:
             print(v2, 'is not present in the graph')
        else:
            self.graph[v1].append(v2)
            self.graph[v2].append(v1)
    
    def delete_node(self, v):
        if v not in self.graph:
            print(v, 'is not present in the graph')
        else:
            self.graph.pop(v)
            for i in self.graph:
                if v in self.graph[i]:
                    self.graph[i].remove(v)

    def delete_edge(self, v1, v2):
        if v1 not in self.graph:
             print(v1, 'is not present in the graph')
        elif v2 not in self.graph:
             print(v2, 'is not present in the graph')
        else:
            if v2 in self.graph[v1]:
                self.graph[v1].remove(v2)
                self.graph[v2].remove(v1)
    
    def print_graph(self):
        print(end="  ")
        for i in range(self.node_count):
            print(self.nodes[i], end=" ")
        print()
    
        for i in range(self.node_count):
            print(self.nodes[i], end=" ")
            for j in range(self.node_count):                  
                print(self.graph[i][j], end=" ")
            print()

um = ListRepresentationUndirected()

um.add_node('A')
um.add_node('B')
um.add_node('C')
um.add_node('D')
um.add_node('E')
um.add_node('F')

um.add_edge('A', 'B')
um.add_edge('A', 'D')
um.add_edge('A', 'C')
um.add_edge('B', 'D')
um.add_edge('B', 'E')
um.add_edge('C', 'D')
um.add_edge('D', 'E')
um.add_edge('E', 'F')
# um.delete_node('E')
print(um.graph)

um.delete_edge('E', 'F')

print(um.graph)