from queue import Queue
import numpy


class People:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.isFree = True
        self.engaged = None
        self.likeList = None
        self.likeDir = None
        self.proposedNums = 0

    def proposed(self):
        self.proposedNums += 1

    def toEngaged(self, engaged):
        self.isFree = False
        self.engaged = engaged

    def toUnengaged(self):
        self.isFree = True
        self.engaged = None

    def getLikeList(self, likeList):
        self.likeList = likeList
        self.likeDir = {val: key for key, val in likeList.items()}


def getSuitWoman(man):
    return man.likeList[man.proposedNums]


def isMoreLikeTheMan(woman, man):
    return woman.likeDir[man] < woman.likeDir[woman.engaged]


def engaged(woman, man):
    man.toEngaged(woman)
    woman.toEngaged(man)


def free(woman, man):
    man.toUnengaged()
    woman.toUnengaged()


def getData():
    manName = ['m0', 'm1', 'm2', 'm3', 'm4', 'm5', 'm6', 'm7', 'm8', 'm9']
    womanName = ['w0', 'w1', 'w2', 'w3', 'w4', 'w5', 'w6', 'w7', 'w8', 'w9']

    man = "3 9 7 8 4 6 0 5 2 1 " \
            "7 6 9 2 0 3 1 8 5 4 " \
            "8 7 9 3 6 5 0 2 4 1 " \
            "2 7 9 1 0 4 5 3 8 6 " \
            "1 4 0 3 2 5 7 9 6 8 " \
            "1 2 5 7 9 4 0 6 8 3 " \
            "6 1 8 2 5 0 9 3 4 7 " \
            "7 0 1 2 4 5 8 6 9 3 " \
            "0 4 2 8 6 3 5 9 1 7 " \
            "6 9 4 2 0 7 5 8 3 1 "
    woman = "1 3 7 2 9 5 6 8 4 0 " \
          "5 3 9 8 6 0 2 1 4 7 " \
          "6 8 5 0 9 7 3 1 4 2 " \
          "0 4 2 1 5 9 6 3 7 8 " \
          "3 6 1 7 5 8 9 2 4 0 " \
          "1 6 2 5 4 9 0 3 8 7 " \
          "2 3 7 9 8 6 5 1 0 4 " \
          "8 7 1 4 3 6 2 0 9 5 " \
          "1 0 7 2 5 3 6 9 8 4 " \
          "1 5 4 2 0 9 8 6 7 3 "
    manLikeList = numpy.array([int(i) for i in man.split()]).reshape(len(manName), len(womanName)).tolist()
    womanLikeList = numpy.array([int(i) for i in woman.split()]).reshape(len(womanName), len(manName)).tolist()


    # manName = ["Alex", "David", "Bob", "Chris"]
    # womanName = ["Ada", "Becky", "Cindy", "Diana"]
    # manLikeList = [[1, 4, 3, 2],
    #                [3, 1, 2, 4],
    #                [1, 2, 3, 4],
    #                [2, 4, 3, 1]]
    # womanLikeList = [[4, 1, 3, 2],
    #                  [1, 2, 4, 3],
    #                  [3, 2, 4, 1],
    #                  [2, 3, 1, 4]]
    # manLikeList = numpy.array([j - 1 for i in manLikeList for j in i]).reshape(4, 4).tolist()
    # womanLikeList = numpy.array([j - 1 for i in womanLikeList for j in i]).reshape(4, 4).tolist()
    # manLikeList = numpy.array([int(i) for i in man.split()]).reshape(len(manName), len(womanName)).tolist()
    # womanLikeList = numpy.array([int(i) for i in woman.split()]).reshape(len(womanName), len(manName)).tolist()
    return manName, manLikeList, womanName, womanLikeList


def initDate(manName, manLikeList, womanName, womanLikeList):
    manList = [People(name, 1) for name in manName]
    womanList = [People(name, 0) for name in womanName]
    for i in range(len(manList)):
        temp = 0
        dir = {}
        for j in manLikeList[i]:
            dir[temp] = [peop for peop in womanList if peop.name==womanName[j]][0]
            temp += 1
        manList[i].getLikeList(dir)
        dir = {}
        temp = 0
        # for j in womanLikeList[i]:
        #     dir[j] = manList[temp]
        #     temp +=  1
        for j in womanLikeList[i]:
            dir[temp] = [peop for peop in manList if peop.name==manName[j]][0]
            temp += 1
        womanList[i].getLikeList(dir)
    return manList, womanList


def show(manList):
    print('匹配队列：')
    for man in manList:
        print('\t' + man.name + '<--->' + man.engaged.name)


def galeShapley():
    manName, manLikeList, womanName, womanLikeList = getData()
    manList, womanList = initDate(manName, manLikeList, womanName, womanLikeList)
    manQueue = Queue()
    [manQueue.put(man) for man in manList]
    while (manQueue.qsize() > 0):
        man = manQueue.get()
        woman = getSuitWoman(man)
        # print("当前的man：",man.name,",woman:",woman.name,end='-')
        man.proposed()
        if (woman.isFree):
            engaged(woman, man)
            # print('匹配。')
        elif (isMoreLikeTheMan(woman, man)):
            manQueue.put(woman.engaged)
            # print("将",woman.engaged.name,'换成',man.name)
            free(woman, woman.engaged)
            engaged(woman, man)

        else:
            # print('匹配失败')
            manQueue.put(man)
    show(manList)


galeShapley()
