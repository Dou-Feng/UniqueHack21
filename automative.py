import queue

class OperationSet():
    opque = queue.Queue()
    filehandler = None
    ENLARGE_SIZE = 100
    def __init__(self, filename):
        self.filehandler = open(filename, 'r')
        self.fillQue()

    # def fillQue(self):
    #     if not self.filehandler:
    #         return False
    #     l = self.filehandler.readline()
    #     for e in l:
    #         if e == 'L' or e == 'R' or e == 'H':
    #             self.opque.put(e)
    #     return not self.opque.empty()

    def fillQue(self):
        if not self.filehandler:
            return False
        while l := self.filehandler.readline():
            coord = l.split(' ')
            self.opque.put((int(coord[0]), int(coord[1])))


    def getnxt(self):
        if self.opque.empty():
            return None
        # return 'a'
        return self.opque.get(0)
    

    

class DataGen():
    filehandler = None

    def __init__(self, filename):
        self.filehandler = open(filename, "a")
    
    def screenshot(self, p, enemies):
        self.filehandler.write("[")
        self.filehandler.write("[" + str(p[0]) + ", " + str(p[1]) + "]")
        for e in enemies:
            self.filehandler.write(", [" + str(e[0]) + ", " + str(e[1]) + "]")
        self.filehandler.write("]\n")


if __name__ == '__main__':
    # dg = DataGen("data.out")
    # dg.screenshot((10, 10), [(10, 11), (100, 100)])
    ops = OperationSet("input.in")
    while c := ops.getnxt():
        print(c)
