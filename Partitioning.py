class Lecture:
    def __init__(self, id, beginTime, endTime):
        self.id = id
        self.beginTime = beginTime
        self.endTime = endTime

    def __repr__(self):
        return self.id + ',' + str(self.beginTime) + '-' + str(self.endTime)


def initData():
    data = [['A', 9, 10.5], ['B', 9, 12.5], ['C', 9, 10.5], ['D', 11, 12.5], ['E', 11, 14], ['F', 13, 14.5],
            ['G', 13, 14.5], ['H', 14, 16.5], ['I', 15, 16.5], ['J', 15, 16.5]]
    lectureList = []
    for lecture in data:
        lectureList.append(Lecture(lecture[0], lecture[1], lecture[2]))
    return lectureList


def partitioning():
    lectureList = initData()
    l = sorted(lectureList, key=lambda lecture: lecture.beginTime)
    classroomNum = 1
    schedule = [[lectureList[0]]]
    for lecture in lectureList[1:]:
        flag = True
        for classroom in schedule:
            temp = classroom.pop()
            if temp.endTime<=lecture.beginTime:
                classroom.append(temp)
                classroom.append(lecture)
                flag = False
                break
            else:
                classroom.append(temp)

        if flag:
            schedule.append([lecture])
            classroomNum += 1


    for i in schedule:
        print(':',end='')
        for j in i:
            print(j.id,end='')
        print()


partitioning()