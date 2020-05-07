from queue import PriorityQueue
from collections import deque
import sys
from copy import deepcopy
import random
import heapq
import queue
import math
from copy import deepcopy


class Graph:
    def __init__(self, fileName):
        """
        :param fileName: the graph is created with the data read from the given file
        """
        self.fileName = fileName
        self._inbound = {}
        self._outbound = {}
        self.__cost = {}
        self._vertices = self.readVertices(fileName)
        self.V = []

        for i in range(0, self._vertices):
            self.V.append(i)

        for i in range(0, self._vertices):
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
            self.__cost[(y, x)] = c
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
        :return: True if the edge exists in.txt the graph, False otherwise
        """
        for i in self._outbound[x]:
            if i == y:
                return True
        return False

    def isVertex(self, x):
        """
        This function verifies if a given vertex exists or not
        :param x: the vertex that will be verified
        :return: True if the vertex exists in.txt the graph, False otherwise
        """
        if x in self.parse():
            return True
        return False

    def addVertex(self, x):
        """
        :param x: the vertex which will be added, if it doesn't already exists in.txt the graph
        :return: True if the vertex was added to the graph, False otherwise
        """
        if not self.isVertex(x):
            self._inbound[x] = []
            self._outbound[x] = []
            return True
        return False

    def removeVertex(self, x):
        """
        :param x: the vertex which will be removed, if it already exists in.txt the graph
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

    def bfs(self, start):
        queue, enqueued = deque([(None, start)]), set([start])
        while queue:
            parent, n = queue.popleft()
            yield parent, n
            new = set(self.parseOutboundNeighbours(n)) - enqueued
            enqueued |= new
            queue.extend([(n, child) for child in new])

    def shortest_path(self, start, end):
        paths = {None: []}
        for parent, child in self.bfs(start):
            paths[child] = paths[parent] + [child]
            if child == end:
                return paths[child], len(paths[child]) - 1
        return None

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

    def BellmanFord(self, src, dest):
        dist = [float("Inf")] * self._vertices
        dist[src] = 0

        # Step 2: Relax all edges |V| - 1 times. A simple shortest
        # path from src to any other vertex can have at-most |V| - 1
        # edges
        for i in range(self._vertices - 1):
            # Update dist value and parent index of the adjacent vertices of
            # the picked vertex. Consider only those vertices which are still in
            # queue
            for u in self._inbound:
                for v in self._outbound[u]:
                    w = self.__cost[(u, v)]
                    if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w

        # Step 3: check for negative-weight cycles.  The above step
        # guarantees shortest distances if graph doesn't contain
        # negative weight cycle.  If we get a shorter path, then there
        # is a cycle.
        for u in self._inbound:
            for v in self._outbound[u]:
                w = self.__cost[(u, v)]
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    print("Graph contains negative weight cycle")

        return dist[dest]

    def bellman(self, source, target):
        previous = {}
        distance = {}
        queue = []
        visited = {}
        count = {}

        cost_dict = self.__cost

        # we initialize the dictionaries
        for node in self.V:
            distance[node] = math.inf
            previous[node] = None
            count[node] = 0
            # no node is visited at the beginning
            visited[node] = False

        # the distance is 0 at the beginning
        distance[source] = 0

        # push the source in the queue
        queue.append(source)

        # the source vertex is marked as visited
        visited[source] = True

        # while the queue is not empty
        while queue:
            vertex = queue[0]
            queue.pop(0)
            visited[vertex] = False  # the vertex is marked as not visited
            for child in self._outbound:  # search through all its neighbours
                if distance[child] > distance[vertex] + cost_dict[(vertex, child)]:
                    distance[child] = distance[vertex] + cost_dict[(vertex, child)]  # update the distance
                    previous[child] = vertex

                    if visited[child] is False:
                        visited[child] = True  # child is marked as true
                        count[child] += 1
                        queue.append(child)  # push the child in the queue

                        # if the number of vertices is greater than the maximum number of vertices,
                        # we have negative cost cycle
                        # if count[child] >= len(self.graph.get_out()):
                        #     print("Negative cost cycle!")
                        #     return None

        # returns a pair distance, path
        msg = "no path"
        if distance[target] == math.inf:
            print("no path")
            return msg
        return (distance[target], self.get_path(source, target, previous))

    def get_path(self, v1, v2, dict):
        lista = []
        node = v2
        while node != v1:
            lista.append(node)
            node = dict[node]
        lista.append(v1)

        lista.reverse()
        return lista

    def getCostPrim(self, list, vertex):
        for el in list:
            if el[1] == vertex:
                return el[0]
        return None

    def prim(self, startVertex):
        verticesCost = []
        prev = {}
        verticesCost.append([0, startVertex])
        prev[startVertex] = -1
        for vert in self.V:
            if vert != startVertex:
                heapq.heappush(verticesCost, [999999999, vert])
                prev[vert] = -1
        mst = []
        minCost = 0
        while len(verticesCost) > 0:
            cost, currentVert = heapq.heappop(verticesCost)
            if prev[currentVert] != -1:
                minCost += cost
                mst.append((prev[currentVert], currentVert))
            for vert in self._outbound[currentVert]:
                verCost = self.getCostPrim(verticesCost, vert)
                if verCost != None:
                    if self.__cost[vert, currentVert] < verCost:
                        verticesCost.remove([verCost, vert])
                        heapq.heappush(verticesCost, [self.__cost[vert, currentVert], vert])
                        prev[vert] = currentVert
        return mst, minCost