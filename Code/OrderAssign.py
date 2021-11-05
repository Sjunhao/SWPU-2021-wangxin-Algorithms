max_path = []      #最大分值的路径
max_cost = 0    #记录最大分值

'''
i:当前的位置
j：当前的层数
orderList：订单列表
path：当前路径
cost：当前路径的分值
'''
def DFS(i, j, orderList, path, cost):
    cost += orderList[j][i]
    if (j == len(orderList) - 1):
        global max_path, max_cost
        if cost > max_cost:
            max_cost = cost
            max_path = path.copy()
        return
    k = 0
    while (k < len(orderList)):
        if k in path:
            k += 1
            continue
        path.append(k)
        DFS(k, j + 1, orderList, path, cost)
        cost -= orderList[k][j + 1]
        path.pop()
        k += 1

'''
将整个订单列表看作是一个图，或者森林，利用深度优先的方式遍历整个搜索空间，
在搜索时候利用订单不能重复派单进行剪枝
'''
def orderAssign():
    orderList = [[1, 2, 4],
                 [7, 11, 16],
                 [37, 29, 22]]
    for i in range(len(orderList)):
        DFS(i, 0, orderList, [i], orderList[0][i])



orderAssign()
print(max_path)
