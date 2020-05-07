# Python Program to detect cycle in an undirected graph
from collections import defaultdict
import sys


# This class represents a undirected graph using adjacency list representation
class UndirectedGraph:

    def __init__(self, fileName):
        self.__cost = {}
        self._weight = 0
        self.V = self.readVertices(fileName)  # No. of vertices
        self.graph = defaultdict(list)  # default dictionary to store graph
        self.answer = []

        self.readFromFile(fileName)
        self.path = []

    @staticmethod
    def readVertices(fileName):
        """
        :param fileName: the file from where the data is read
        :return: the number of vertices of the graph
        """
        f = open(fileName, "r")
        line = f.readline().strip()
        l = line.split(" ")
        return int(l[0])

    def readFromFile(self, fileName):
        """
        :param fileName: the file from where the data is read
        :return: the function adds to the graph every vertex, edge and cost read
        """
        f = open(fileName, "r")
        line = f.readline().strip()
        line = f.readline().strip()
        while len(line) > 2:
            l = line.split(" ")
            x = int(l[0])
            y = int(l[1])
            c = int(l[2])
            self.addEdge(x, y, c)
            line = f.readline().strip()

    # function to add an edge to graph
    def addEdge(self, v, w, c):
        self.graph[v].append(w)  # Add w to v_s list
        self.graph[w].append(v)  # Add v to w_s list
        self.__cost[(v, w)] = c

    def printGraph(self):
        for i in self.graph:
            for j in self.graph[i]:
                print(i, "->", j, "having the cost:", self.__cost[(i, j)])

    # Function to find the minimum weight
    # Hamiltonian Cycle
    def minimumHamiltonianCycle(self, v, currPos, n, count, cost, path):

        # If last node is reached and it has
        # a link to the starting node i.e
        # the source then keep the minimum
        # value out of the total cost of
        # traversal and "ans"
        # Finally return to check for
        # more possible values
        if count == n and 0 in self.graph[currPos]:
            try:
                self.answer.append(cost + self.__cost[(currPos, 0)])
                return
            except KeyError:
                self.answer.append(cost + self.__cost[(0, currPos)])
                return

        # BACKTRACKING STEP
        # Loop to traverse the adjacency list
        # of currPos node and increasing the count
        # by 1 and cost by graph[currPos][i] value
        for i in range(n):
            if v[i] is False and i in self.graph[currPos]:
                # Mark as visited
                v[i] = True
                try:
                    self.minimumHamiltonianCycle(v, i, n, count + 1, cost + self.__cost[(currPos, i)], path)
                    path.append(currPos)
                except KeyError:
                    self.minimumHamiltonianCycle(v, i, n, count + 1, cost + self.__cost[(i, currPos)], path)
                    path.append(currPos)

                # Mark ith node as unvisited
                v[i] = False

    def findMinimumPath(self):
        path = []
        a = []
        v = [False for i in range(self.V)]
        # Mark 0th node as visited
        v[0] = True
        # Find the minimum weight Hamiltonian Cycle
        self.minimumHamiltonianCycle(v, 0, self.V, 1, 0, path)

        for x in self.answer:
            if x not in a:
                a.append(x)
        # ans is the minimum weight Hamiltonian Cycle
        print(min(self.answer), a)
