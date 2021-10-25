class Graph:
    def __init__(self, vertex=[]):
        self.vertex = vertex
        self.vertexNums = len(vertex)

    def addVertex(self, vertex):
        self.vertex.append(vertex)
        self.vertexNums += 1

    def __repr__(self):
        for i in self.vertex:
            print(i)
        return ''

class Vertex:
    def __init__(self, id, neighbor={}):
        self.id = id
        self.neighbor = {}
        # self.neighbor = neighbor

    def addNeighbor(self, nVertex, value):
        self.neighbor[nVertex] = value

    def __repr__(self):
        print(self.id,end=':')
        for i,v in self.neighbor.items():
            print(i.id,v,end=',')
        return ''

def becomeNeighbor(v1,v2,value):
    v1.addNeighbor(v2,value)
    v2.addNeighbor(v1,value)

def initData():
    vertexList = [Vertex('v'+str(i)) for i in range(13)]
    becomeNeighbor(vertexList[0],vertexList[1],2)
    becomeNeighbor(vertexList[0],vertexList[2],4)
    becomeNeighbor(vertexList[1],vertexList[3],7)
    becomeNeighbor(vertexList[1],vertexList[2],5)
    becomeNeighbor(vertexList[2],vertexList[8],4)
    becomeNeighbor(vertexList[2],vertexList[4],3)
    becomeNeighbor(vertexList[2],vertexList[5],1)
    becomeNeighbor(vertexList[3],vertexList[10],1)
    becomeNeighbor(vertexList[3],vertexList[6],6)
    becomeNeighbor(vertexList[3],vertexList[8],3)
    becomeNeighbor(vertexList[4],vertexList[5],5)
    becomeNeighbor(vertexList[5],vertexList[9],8)
    becomeNeighbor(vertexList[7],vertexList[10],4)
    becomeNeighbor(vertexList[7],vertexList[11],5)
    becomeNeighbor(vertexList[8],vertexList[12],8)
    becomeNeighbor(vertexList[10],vertexList[11],10)
    becomeNeighbor(vertexList[11],vertexList[12],2)
    return Graph(vertexList)

def getMin(Q, dist):
    min = Q[0]
    for i in Q[1:]:
        if dist[min] > dist[i]:
            min = i
    Q.remove(min)
    return min

def Dijkstra():
    G = initData()
    print(G)
    Q = []
    dist = {}
    prev = {}
    for v in G.vertex:
        dist[v] = float('inf')
        prev[v] = -1
        Q.append(v)
    dist[G.vertex[0]] = 0

    while len(Q) > 0:
        u = getMin(Q, dist)
        for v,value in u.neighbor.items():
            alt = dist[u] + value
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u
    for v,lenth in dist.items():
        print(v.id,lenth)

Dijkstra()