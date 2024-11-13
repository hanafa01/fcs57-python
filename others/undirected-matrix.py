class MatrixRepresentationUndirected:

    # def __init__(self, v):
    def __init__(self):
        self.nodes = []
        self.graph = []
        self.node_count = 0
        # for i in range(v):
        #     self.graph.append([0] * v)
    
    def add_node(self, v):
        if v in self.nodes:
            print(v, 'is already present in the graph')
        else:
            self.node_count += 1
            self.nodes.append(v)

            for n in self.graph:
                n.append(0)
            
            # temp = []
            # for i in range(self.node_count):
            #     temp.append(0)
            
            # self.graph.append(temp)
            self.graph.append([0] * self.node_count)
    
    def add_edge(self, v1, v2):
        if v1 not in self.nodes:
             print(v1, 'is not present in the graph')
        elif v2 not in self.nodes:
             print(v2, 'is not present in the graph')
        else:
            index1 = self.nodes.index(v1)
            index2 = self.nodes.index(v2)
            self.graph[index1][index2] = 1
            self.graph[index2][index1] = 1
    
    def delete_node(self, v):
        if v not in self.nodes:
            print(v, 'is not present in the graph')
        else:
            index1 = self.nodes.index(v)
            self.node_count -= 1
            self.nodes.remove(v)
            self.graph.pop(index1)
            for i in self.graph:
                i.pop(index1)

    def delete_edge(self, v1, v2):
        if v1 not in self.nodes:
             print(v1, 'is not present in the graph')
        elif v2 not in self.nodes:
             print(v2, 'is not present in the graph')
        else:
            index1 = self.nodes.index(v1)
            index2 = self.nodes.index(v2)
            self.graph[index1][index2] = 0
            self.graph[index2][index1] = 0
    
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

        # for i in self.graph:
        #     print(i)

um = MatrixRepresentationUndirected()
# um = MatrixRepresentationUndirected(4)

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
um.delete_node('E')
um.print_graph()