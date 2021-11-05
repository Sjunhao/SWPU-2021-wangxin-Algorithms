import operator


def initData():
    U = [i + 1 for i in range(30)]
    cost = [1 for i in range(30)]
    subsets = []
    subsets.append([1, 2, 3, 4, 5, 6, 7, 8])
    subsets.append([9, 10, 11, 12])
    subsets.append([13, 14])
    subsets.append([1, 2, 3, 4, 9, 10, 13,15,16,17,18,19,20,21,22])
    subsets.append([5, 6, 7, 8, 11, 12, 14,23,24,25,26,27,28,29,30])
    subsets.append([15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30])
    return U, subsets, cost

# def initData():
#     U = [i + 1 for i in range(9)]
#     cost = [1 for i in range(9)]
#     subsets = []
#     subsets.append([1,2,3])
#     subsets.append([1,2,3,4])
#     subsets.append([4,9])
#     subsets.append([5,6])
#     subsets.append([5,7])
#     subsets.append([5, 6, 7, 8])
#     subsets.append([7, 8])
#     return U, subsets, cost

def getMaxSet(subsets, C, cost):
    max = 0
    flag = 0
    loc = 0
    for _set in subsets:
        temp = 0
        for i in _set:
            temp += cost[i - 1]
        if temp > max:
            max = temp
            loc = flag
        flag += 1
    return loc, max

# def getSubSet(subsets, C, cost):
#     min = 100
#     flag = 0
#     loc = 0
#     for _set in subsets:
#         temp = 0
#         for i in _set:
#             temp += cost[i - 1]
#         if temp < min:
#             min = temp
#             loc = flag
#         flag += 1
#     return loc, min


def SetCover():
    U, subsets, cost = initData()
    u = set(U)
    C = set()
    pickSets = []
    print("U:", U, "\nsubsets:", subsets)
    while operator.ne(C, u):
        # S_loc, S_cost = getSubSet(subsets, C, cost) #当前权重和最大的子序列
        S_loc, S_cost = getMaxSet(subsets, C, cost) #当前权重和最大的子序列
        temp = set(subsets[S_loc]) - C              #当前子序列中未选中的节点
        # # a = S_cost / len(temp)
        # a = len(temp)/S_cost
        # print(S_cost, len(temp))
        # for i in temp:
        #     cost[i - 1] = 1     #调整当前已选择节点的权重
        C = C | temp            #合并新的选中节点
        pickSets.append(subsets[S_loc].copy())      #记录已选择的子序列
        del subsets[S_loc]
        # print(subsets)
    print("picked sets：", pickSets)


SetCover()
