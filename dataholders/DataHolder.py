
class DataHolder:
    def __init__(self, maxsize=10, defaultval=0):
        self.hasNew = True
        self.datas = [defaultval for i in range(maxsize)]
        self.max = maxsize

    def push(self, data):
        self.datas.append(data)
        self.hasNew = True
        if len(self.datas) > self.max:
            self.datas = self.datas[1:]

    def isnew(self) -> bool:
        return self.hasNew

    def getdata(self):
        self.hasNew = False
        return self.datas

    def top(self):
        return self.datas[-1]
