from queue import Queue


class vertex:
    def __init__(self, id):
        self.id = id
        self.edge = {}

    def addEdge(self, edge, weight):
        self.edge[edge] = weight


class Graph:
    def __init__(self):
        self.vertex = {}
        self.vertexNums = 0

    def addVertex(self, id, weight):
        self.vertex[id] = weight
        self.vertexNums += 1


def initData():
    g = [[0, 1, 0, 1, 1],
         [1, 0, 1, 1, 1],
         [0, 1, 0, 0, 0],
         [1, 1, 0, 1, 1],
         [1, 1, 0, 1, 0]]
    G = Graph()
    [G.addVertex(vertex(id), 1) for id in range(len(g))]
    [v.addEdge(i, 1) for v in G.vertex.keys() for i in range(len(g[v.id])) if g[v.id][i]]
    return G


def BFS(v, vertexDir):
    discovered = {}
    queue = Queue()
    discovered[v.id] = 1
    queue.put(v)
    while queue.qsize() > 0:
        u = queue.get()
        for s in u.edge:
            if discovered.get(s, 0) == 0:
                discovered[s] = 1
                queue.put(vertexDir[s])
        print(str(u.id) + '->', end='')


def DFS_(v, vertexDir):
    discovered = {}
    stack = []
    discovered[v.id] = 1
    print(str(v.id) + '->', end='')
    stack.append(v)
    while len(stack) > 0:
        u = stack.pop()
        for s in u.edge:
            if discovered.get(s, 0)==0:
                discovered[s]=1
                stack.append(u)
                stack.append(vertexDir[s])
                print(str(vertexDir[s].id) + '->', end='')
                continue



def DFS(v, vertexDir, discovered={}):
    discovered[v.id] = 1
    print(str(v.id) + '->', end='')
    for s in v.edge:
        if discovered.get(s, 0) == 0:
            discovered[s] = 1
            DFS(vertexDir[s], vertexDir, discovered)


def GraphSearch():
    G = initData()
    vertexDir = {v.id: v for v in list(G.vertex.keys())}
    BFS(vertexDir[0], vertexDir)
    print()
    DFS(vertexDir[0], vertexDir)
    print()
    DFS_(vertexDir[0], vertexDir)


GraphSearch()
