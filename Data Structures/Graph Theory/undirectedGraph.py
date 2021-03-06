"""
Implementation of Undirected Graph
"""
from sys import maxsize
INFINITY = maxsize

class Vertex:
    def __init__(self, label):
        self.label = str(label)
        self.adjList = {}
        self.color = "white"
        self.distance = maxsize
        self.predecessor = None

    def addNeighbour(self, toVertex, cost = 0):
        self.adjList[toVertex] = cost

    def getConnections(self):
        return self.adjList.keys()

    def getLabel(self):
        return self.label

    def getCost(self, toVertex):
        return self.adjList[toVertex]

    def setColor(self, colorValue):
        self.color = colorValue

    def getColor(self):
        return self.color

    def __str__(self):
        return self.label + " connected to " + str([x for x in self.adjList])


class Graph:
    def __init__(self):
        self.verticesList = {}
        self.numVertices = 0

    def addVertex(self, label):
        self.numVertices += 1
        newVertex = Vertex(label)
        self.verticesList[label] = newVertex
        return newVertex

    def addEdge(self, firstVertex, secondVertex, cost = 0):
        if firstVertex not in self.verticesList:
            firstNewVertex = self.addVertex(firstVertex)
        if secondVertex not in self.verticesList:
            secondNewVertex = self.addVertex(secondVertex)
        self.verticesList[firstVertex].addNeighbour(secondVertex, cost)
        self.verticesList[secondVertex].addNeighbour(firstVertex, cost)

    def getVertices(self):
        return self.verticesList.keys()

    def verticesCount(self):
        return self.numVertices

    def displayGraph(self):
        for vertex in self.verticesList:
            print (self.verticesList[vertex])



# Testcase - Undirected graph
def testcases():
    g = Graph()

    for i in range(6):
        g.addVertex(chr(ord('A') + i))

    g.addEdge('A', 'B', 5)
    g.addEdge('A', 'D', 9)
    g.addEdge('A', 'E', 2)
    g.addEdge('B', 'C', 2)
    g.addEdge('C', 'D', 3)
    g.addEdge('D', 'F', 2)
    g.addEdge('E', 'F', 3)

    # print (g.getVertices())
    # print (g.verticesCount())
    # g.displayGraph()

    return g
