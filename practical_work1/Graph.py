

class Graph:
    def __init__(self, fileName):
        """
        :param fileName: the graph is created with the data read from the given file
        """
        self._inbound = {}
        self._outbound = {}
        self.__cost = {}
        self.__vertices = self.readVertices(fileName)

        for i in range(0, self.__vertices):
            self._inbound[i] = []
            self._outbound[i] = []
        self.readFromFile(fileName)

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

    def getNumber(self):
        """
        :return: the number of vertices of the graph
        """
        return len(self._inbound.keys())

    def parse(self):
        """
        The function parses the whole graph
        """
        return list(self._inbound.keys())

    def parseInboundNeighbours(self, x):
        """
        :param x: the vertex which inbound edges will be parsed
        :return: the parsed inbound edges
        """
        if self.isVertex(x):
            return self._inbound[x]
        return False

    def parseOutboundNeighbours(self, x):
        """
        :param x: the vertex which outbound edges will be parsed
        :return: the parsed outbound edges
        """
        if self.isVertex(x):
            return self._outbound[x]
        return False

    def addEdge(self, x, y, c):
        """
        :param x: the first end of the edge that will be added
        :param y: the second end of the edge that will be added
        :param c: the cost of the pair x and y
        :return: True if the edge was added to the graph, False otherwise
        """
        if not self.isEdge(x, y):
            self._inbound[y].append(x)
            self._outbound[x].append(y)
            self.__cost[(x, y)] = c
            return True
        return False

    def removeEdge(self, x, y):
        """
        :param x: the first end of the edge that will be removed
        :param y: the second end of the edge that will be removed
        :return: True if the edge was removed from the graph, False otherwise
        """
        if self.isEdge(x, y):
            self._inbound[y].remove(x)
            self._outbound[x].remove(y)
            del self.__cost[(x, y)]
            return True
        return False

    def isEdge(self, x, y):
        """
        This function verifies if a given edge exists or not
        :param x: the first end of the edge that will be verified
        :param y: the second end of the edge that will be verified
        :return: True if the edge exists in the graph, False otherwise
        """
        for i in self._outbound[x]:
            if i == y:
                return True
        return False

    def isVertex(self, x):
        """
        This function verifies if a given vertex exists or not
        :param x: the vertex that will be verified
        :return: True if the vertex exists in the graph, False otherwise
        """
        if x in self.parse():
            return True
        return False

    def addVertex(self, x):
        """
        :param x: the vertex which will be added, if it doesn't already exists in the graph
        :return: True if the vertex was added to the graph, False otherwise
        """
        if not self.isVertex(x):
            self._inbound[x] = []
            self._outbound[x] = []
            return True
        return False

    def removeVertex(self, x):
        """
        :param x: the vertex which will be removed, if it already exists in the graph
        :return: True if the vertex was removed from the graph, False otherwise
        """
        if self.isVertex(x):
            for i in self.parseInboundNeighbours(x):
                self.removeEdge(i, x)
            for i in self.parseOutboundNeighbours(x):
                self.removeEdge(x, i)
            del self._inbound[x]
            del self._outbound[x]
            return True
        return False

    def getCost(self, x, y):
        """
        :param x: the first end of the edge
        :param y: the second end of the edge
        :return: the value of the cost between the vertices
        """
        if self.isEdge(x, y):
            return self.__cost[(x, y)]
        return False

    def setCost(self, x, y, new_cost):
        """
        :param x: the first end of the edge
        :param y: the second end of the edge
        :param new_cost: the new value of the cost
        :return: True if the old value of the cost was replaced with the new value
        """
        if self.isEdge(x, y):
            self.__cost[(x, y)] = new_cost
            return True
        return False

    def printGraph(self):
        for i in self.parse():
            if len(self._inbound[i]) == len(self._outbound[i]) == 0:
                print(i, "is an isolated vertex")
            else:
                for j in self._outbound[i]:
                    print(i, "->", j, "having the cost:", self.__cost[(i, j)])
