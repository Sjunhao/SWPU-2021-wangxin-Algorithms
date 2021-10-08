class Edge:
    def __init__(self, id, vA, vB, weight):
        self.id = id
        self.vA = vA
        self.vB = vB
        self.weight = weight

    def __repr__(self):
        return str(self.id) + str(self.vA) + str(self.vB) + str(self.weight)


def kruskal():
    G = [[-1, 6, 1, 5, 0, 0],
         [6, -1, 5, 0, 3, 0],
         [0, 5, -1, 5, 6, 4],
         [5, 0, 5, -1, 0, 2],
         [0, 3, 6, 0, -1, 6],
         [0, 0, 4, 2, 6, -1]]
    Gvid = ['A', 'B', 'C', 'D', 'E', 'F']
    T = []
    edgeList = [Edge(i + j, i, j, G[i][j]) for i in range(0, len(G)) for j in range(i + 1, len(G[i])) if G[i][j] != 0]
    edgeList = sorted(edgeList, key=lambda edge: edge.weight)
    tempSet = [set([i]) for i in range(len(G))]
    for edge in edgeList:
        vAloc = 0
        vBloc = 0
        for i in range(len(tempSet)):
            if edge.vA in tempSet[i]:
                vAloc = i
            if edge.vB in tempSet[i]:
                vBloc = i
        if vBloc == vAloc:
            continue
        else:
            T.append(edge)
            tempSet[vAloc] = tempSet[vAloc].union(tempSet[vBloc])
            del tempSet[vBloc]

    for edge in T:
        print('边%s连接边%s权重为%d' % (Gvid[edge.vA], Gvid[edge.vB], edge.weight))


kruskal()
