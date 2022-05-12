from copy import deepcopy


class Jigsaw:
    def __init__(self, height, width, jigsawArray, zeroPos, path):
        self.height = height
        self.width = width
        self.solved = False
        self.actualArray = jigsawArray
        if zeroPos == None:
            self.findZeroPosition()
        else:
            self.zeroPosition = zeroPos
        self.path = path

    def getPath(self):
        return self.path

    def findZeroPosition(self):
        for x in range(self.height * self.width):
            if self.actualArray[x] == 0:
                self.zeroPosition = x

    def swapUp(self):
        changedArray = deepcopy(self.actualArray)
        if(self.zeroPosition < self.width-1):
            return None
        else:
            tmp = changedArray[self.zeroPosition - self.width]
            changedArray[self.zeroPosition - self.width] = 0
            changedArray[self.zeroPosition] = tmp
            nextZeroPos = self.zeroPosition - self.width
            return Jigsaw(self.height, self.width, changedArray, nextZeroPos, self.path + "U")

    def swapDown(self):
        changedArray = deepcopy(self.actualArray)
        if self.zeroPosition > (((self.height - 1)*self.width) - 1):
            return None
        else:
            tmp = changedArray[self.zeroPosition + self.width]
            changedArray[self.zeroPosition + self.width] = 0
            changedArray[self.zeroPosition] = tmp
            nextZeroPos = self.zeroPosition + self.width
            return Jigsaw(self.height, self.width, changedArray, nextZeroPos, self.path + "D")

    def swapLeft(self):
        changedArray = deepcopy(self.actualArray)
        if(self.zeroPosition % self.width == 0):
            return None
        else:
            tmp = changedArray[self.zeroPosition - 1]
            changedArray[self.zeroPosition-1] = 0
            changedArray[self.zeroPosition] = tmp
            nextZeroPos = self.zeroPosition-1
            return Jigsaw(self.height, self.width, changedArray, nextZeroPos, self.path + "L")

    def swapRight(self):
        changedArray = deepcopy(self.actualArray)
        if(self.zeroPosition % self.width == (self.width-1)):
            return None
        else:
            tmp = self.actualArray[self.zeroPosition+1]
            changedArray[self.zeroPosition+1] = 0
            changedArray[self.zeroPosition] = tmp
            nextZeroPos = self.zeroPosition + 1
            return Jigsaw(self.height, self.width, changedArray, nextZeroPos, self.path + "R")


def correctSolution(w, h):
    solution = []
    value = 1
    for x in range(h*w):
        solution.append(value)
        value = value + 1
        if(x == (h*w)-1):
            solution[x] = 0
    return solution
