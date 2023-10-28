class Graph:

    def __init__(self):

        self.adjacency_list = {}

    def add_vertex(self,vertex):

        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = []
            return True
        return False
    

    def print_graph(self):

        for vertex in self.adjacency_list:
            print(vertex, ":", self.adjacency_list[vertex])


    def add_edge(self, vertex1, vertex2):


        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():

            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
            return True

        return False

    def remove_edge(self,vertex1, vertex2):

        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():

            self.adjacency_list[vertex1].remove(vertex2)
            self.adjacency_list[vertex2].remove(vertex1)

            return True 

        return False


my_graph = Graph()

my_graph.add_vertex("A")
my_graph.add_vertex("B")
my_graph.add_vertex("C")

my_graph.add_edge("A","B")
my_graph.add_edge("A","C")
my_graph.add_edge("B","C")
my_graph.print_graph()



my_graph.remove_edge("A", "C")

print("after removing edge")
my_graph.print_graph()