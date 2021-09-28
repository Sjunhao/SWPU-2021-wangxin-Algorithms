class Jobs:
    def __init__(self, id, beginTime, endTime):
        self.id = id
        self.beginTime = beginTime
        self.endTime = endTime

    def __repr__(self):
        return str(self.id) + str(self.beginTime) + str(self.endTime)


def initData():
    # data = [[1, 5], [1, 7], [0, 6], [1, 3], [2, 9], [3, 6], [4, 7], [4, 6]]
    data = [[0, 6], [1, 4], [3, 5], [3, 8], [4, 7], [5, 9], [6, 10], [8, 11]]
    jobList = []
    for i in range(len(data)):
        jobList.append(Jobs(i, data[i][0], data[i][1]))
    return jobList


def intervalScheduling():
    jobList = initData()
    l = sorted(jobList, key=lambda job: job.endTime)
    ans = [l[0]]
    flag = 0
    for job in l[1:]:
        if job.beginTime < ans[flag].endTime:
            continue
        ans.append(job)
        flag += 1
    print('Job List:')
    for job in ans:
        print(job.id,end=' ')



intervalScheduling()
