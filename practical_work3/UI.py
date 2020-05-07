from Graph import Graph
from prim import PrimsAlgorithm
from hamiltonian import UndirectedGraph


class UI:
    def __init__(self, fileName):
        self.graph = Graph(fileName)

    @staticmethod
    def menu():
        str = ""
        str += "\t  0. exit \n"
        str += "\t  1. get the number of vertices \n"
        str += "\t  2. parse the set of vertices \n"
        str += "\t  3. find out if there is an edge from a vertex to other \n"
        str += "\t  4. get the in.txt and out degree of a vertex \n"
        str += "\t  5. parse the set of outbound edges of a vertex \n"
        str += "\t  6. parse the set of inbound edges of a vertex \n"
        str += "\t  7. retrieve or modify the information attached to a specified edge. \n"
        str += "\t  8. add an edge \n"
        str += "\t  9. remove an edge \n"
        str += "\t 10. add a vertex \n"
        str += "\t 11. remove a vertex \n"
        str += "\t 12. print the graph \n"
        str += "\t 13. find shortest path between two vertices \n"
        str += "\t 14. find lowest cost walk between two vertices\n"
        str += "\t 15. construct a minimal spanning tree using the Prim's algorithm\n"
        str += "\t 16. minimum Hamiltonian cycle\n"

        return str

    def run(self):
        print(self.menu())
        while True:

            command = int(input("Enter command: "))

            if command == 0:
                return

            elif command == 1:
                print("Number of vertices:", self.graph.getNumber())

            elif command == 2:
                print(self.graph.parse())

            elif command == 3:
                first = int(input("Give first vertex: "))
                if not self.graph.isVertex(first):
                    print("The vertex does not exist!")
                    continue

                second = int(input("Give second vertex: "))
                if not self.graph.isVertex(second):
                    print("The vertex does not exist!")
                    continue

                if self.graph.isEdge(first, second):
                    print("The edge exists!")
                else:
                    print("The edge does not exist!")

            elif command == 4:
                vertex = int(input("Give vertex: "))
                for key in self.graph._outbound.keys():
                    if key == vertex:
                        print("Out degree: " + str(len(self.graph._outbound[key])))

                for key in self.graph._inbound.keys():
                    if key == vertex:
                        print("In degree: " + str(len(self.graph._inbound[key])))

            elif command == 5:
                vertex = int(input("Give vertex: "))
                if self.graph.parseOutboundNeighbours(vertex):
                    print(self.graph.parseOutboundNeighbours(vertex))
                else:
                    print("The vertex does not exist!")

            elif command == 6:
                vertex = int(input("Give vertex: "))
                if self.graph.parseInboundNeighbours(vertex):
                    print(self.graph.parseInboundNeighbours(vertex))
                else:
                    print("The vertex does not exist!")

            elif command == 7:
                first = int(input("Give first vertex: "))
                if not self.graph.isVertex(first):
                    print("The vertex does not exist!")
                    continue

                second = int(input("Give second vertex: "))
                if not self.graph.isVertex(second):
                    print("The vertex does not exist!")
                    continue

                print(self.graph.getCost(first, second))

                new_cost = int(input("Give new cost: "))
                if not self.graph.setCost(first, second, new_cost):
                    print("The edge does not exist!")
                else:
                    print("Cost modified successfully!")

            elif command == 8:
                first = int(input("Give first vertex: "))

                if not self.graph.isVertex(first):
                    print("The vertex does not exist!")
                    continue

                second = int(input("Give second vertex: "))
                if not self.graph.isVertex(second):
                    print("The vertex does not exist!")
                    continue

                cost = int(input("Give cost: "))
                if not self.graph.addEdge(first, second, cost):
                    print("The edge already exists!")
                else:
                    print("Edge added successfully")

            elif command == 9:
                first = int(input("Give first vertex: "))
                if not self.graph.isVertex(first):
                    print("The vertex does not exist!")
                    continue

                second = int(input("Give second vertex: "))
                if not self.graph.isVertex(second):
                    print("The vertex does not exist!")
                    continue

                if not self.graph.removeEdge(first, second):
                    print("The edge does not exist!")
                else:
                    print("Edge removed successfully!")

            elif command == 10:
                vertex = int(input("Give vertex: "))
                if not self.graph.addVertex(vertex):
                    print("The vertex already exists!")
                else:
                    print("Vertex added successfully")

            elif command == 11:
                vertex = int(input("Give vertex: "))
                if not self.graph.removeVertex(vertex):
                    print("The vertex does not exist!")
                else:
                    print("Vertex has been removed!")

            elif command == 12:
                self.graph.printGraph()

            elif command == 13:
                first = int(input("Add first vertex: "))
                second = int(input("Add second vertex: "))
                print(self.graph.shortest_path(first, second))

            elif command == 14:
                first = int(input("Add first vertex: "))
                second = int(input("Add second vertex: "))
                print(self.graph.BellmanFord(first, second))
                # print(self.graph.bellman(first, second))

            elif command == 15:
                # self.graph.prim(0)
                PrimsAlgorithm()
            elif command == 16:
                graph = UndirectedGraph("input.txt")
                graph.findMinimumPath()
