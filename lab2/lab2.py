class Graph:
    def __init__(self, nodeList):
        self.nodesDict = nodeList
        self.startNode = ""
        self.endNode = ""

    def addNode(self, node):
        self.nodesDict.append(node)

    def showNodes(self):
        print(self.nodesDict)

    def setStartNode(self, startnode):
        self.startNode = startnode

    def setEndNode(self, endNode):
        self.endNode = endNode

    def dijkstra2(self):
        visited = []
        notVisited = []
        pathDict = {}
        nodeDict = {}
        currNode = "A"

        for key, value in self.nodesDict.items():
            pathDict[key] = 1000
            notVisited.append(key)

        pathDict[self.startNode] = 0

        cont = True

        while cont:
            for key, value in self.nodesDict[currNode].items():
                if key not in visited:
                    if(pathDict[key] > pathDict[currNode] + value):
                        pathDict[key] = pathDict[currNode] + value
                        nodeDict[key] = currNode
            visited.append(currNode)
            notVisited.remove(currNode)

            temp = {}
            for el in notVisited:
                temp[el] = pathDict[el]


            if len(temp) == 0:
                break

            currNode = min(temp, key=temp.get)

            if currNode == self.endNode:
                break

        go = True
        returnNodeList = []
        nextNode = self.endNode

        while go:
            returnNodeList.append(nextNode)
            nextNode = nodeDict[nextNode]

            if nextNode == self.startNode:
                returnNodeList.append(self.startNode)
                go = False



        returnNodeList.reverse()

        return returnNodeList

    def dijkstra(self):
        S = {}
        i = 0


        for key, value in self.nodesDict.items():
            print(value)
            nextNode = min(self.nodesDict[self.startNode], key=self.nodesDict[self.startNode].get)
            i += 1
            S[nextNode] = i


        S[self.startNode] = 0


        print(S)


class Node:
    def __init__(self, name, conn):
        self.name = name
        self.connections = conn

    def addConnection(self, name, weight):
        self.connections[name] = weight

    def showConnections(self):
        print(self.connections)


nodeA = Node('A', {'C': 1, 'D': 2})
nodeB = Node('B', {'F': 3, 'C': 2})
nodeC = Node('C', {'A': 1, 'B': 2, 'D': 1, 'E': 3})
nodeD = Node('D', {'A': 2, 'C': 1, 'G': 1})
nodeE = Node('E', {'C': 3, 'F': 2})
nodeF = Node('F', {'E': 2, 'G': 1})
nodeG = Node('G', {'D': 1, 'F': 1})

nodeList = {}
nodeList['A'] = {'C': 1, 'D': 2}
nodeList['B'] = {'F': 3, 'C': 2}
nodeList['C'] = {'A': 1, 'B': 2, 'D': 1, 'E': 3}
nodeList['D'] = {'A': 2, 'C': 1, 'G': 1}
nodeList['E'] = {'C': 3, 'F': 2}
nodeList['F'] = {'E': 2, 'G': 1}
nodeList['G'] = {'D': 1, 'F': 1}

graph = Graph(nodeList)
# graph.showNodes()
graph.setStartNode('A')
graph.setEndNode('F')
path = graph.dijkstra2()
print(path)

