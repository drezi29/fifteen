class jigsawReader:
    def __init__(self, fileName):
        self.readFile(fileName)
        self.readSize()
        self.readJigsaw()

    def readFile(self, fileName):
        f = open(fileName, "r")
        if f.mode == 'r':
            self.data = f.readlines()
        f.close()

    def readSize(self):
        line = self.data[0].split(' ')
        tmp = line[1]
        tmp = tmp.split('\n')
        line[1] = tmp[0]
        self.height = int(line[0])
        self.width = int(line[1])

    def readJigsaw(self):
        jigsawStr = []
        for x in range(int(self.height)):
            line = self.data[x+1].split(' ')
            tmp = line[int(self.width)-1]
            tmp = tmp.split('\n')
            line[int(self.width)-1] = tmp[0]
            jigsawStr.append(line)

        self.jigsaw = [None] * (int(self.height)*int(self.width))
        for x in range(int(self.height)):
            for y in range(int(self.width)):
                self.jigsaw[(self.width * x) + y] = int(jigsawStr[x][y])
