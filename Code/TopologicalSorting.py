def getNoIncomingEdge(tempG, S, L):
    for i in range(len(tempG)):
        if i in S or i in L:
            continue
        flag = True
        for j in range(len(tempG[i])):
            if tempG[j][i] != 0:
                flag = False
                break
        if flag:
            S.append(i)

###推荐用邻接表
def TopologicalSorting():
    G = [[0, 1, 1, 1, 0, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 1, 0],
         [0, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 1, 0]]
    # G = [[0, 1, 1, 1, 0, 0, 1],
    #      [0, 0, 0, 0, 0, 0, 0],
    #      [0, 1, 0, 0, 0, 0, 0],
    #      [0, 0, 0, 0, 1, 0, 0],
    #      [0, 0, 0, 0, 0, 0, 0],
    #      [0, 0, 0, 1, 1, 0, 0],
    #      [1, 0, 0, 0, 0, 0, 0]]
    tempG = list(G)
    L = []
    S = []
    getNoIncomingEdge(tempG, S, L)
    while len(S) > 0:
        n = S.pop()
        L.append(n)
        for i in range(len(tempG[n])):
            tempG[n][i] = 0
        getNoIncomingEdge(tempG, S, L)
    flag = True
    for l in tempG:
        for i in l:
            if i != 0:
                flag = False
                break
    if flag:
        print(L)
    else:
        print('Error!')


TopologicalSorting()
