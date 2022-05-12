from Jigsaw import *
import math


class JigsawWithHeuristic(Jigsaw):
    def __init__(self, height, width, jigsawArray, zeroPos, path, heuristic):
        super().__init__(height, width, jigsawArray, zeroPos, path)
        self.heuristic = heuristic
        self.heuristicValue = self.calculateHeuristicValue()
        self.fCost = self.heuristicValue + len(self.path)

    def swapUp(self):
        changedArray = deepcopy(self.actualArray)
        if(self.zeroPosition < self.width-1):
            return None
        else:
            tmp = changedArray[self.zeroPosition - self.width]
            changedArray[self.zeroPosition - self.width] = 0
            changedArray[self.zeroPosition] = tmp
            nextZeroPos = self.zeroPosition - self.width
            return JigsawWithHeuristic(self.height, self.width, changedArray, nextZeroPos, self.path + "U", self.heuristic)

    def swapDown(self):
        changedArray = deepcopy(self.actualArray)
        if self.zeroPosition > (((self.height - 1)*self.width) - 1):
            return None
        else:
            tmp = changedArray[self.zeroPosition + self.width]
            changedArray[self.zeroPosition + self.width] = 0
            changedArray[self.zeroPosition] = tmp
            nextZeroPos = self.zeroPosition + self.width
            return JigsawWithHeuristic(self.height, self.width, changedArray, nextZeroPos, self.path + "D", self.heuristic)

    def swapLeft(self):
        changedArray = deepcopy(self.actualArray)
        if(self.zeroPosition % self.width == 0):
            return None
        else:
            tmp = changedArray[self.zeroPosition - 1]
            changedArray[self.zeroPosition-1] = 0
            changedArray[self.zeroPosition] = tmp
            nextZeroPos = self.zeroPosition-1
            return JigsawWithHeuristic(self.height, self.width, changedArray, nextZeroPos, self.path + "L", self.heuristic)

    def swapRight(self):
        changedArray = deepcopy(self.actualArray)
        if(self.zeroPosition % self.width == (self.width-1)):
            return None
        else:
            tmp = changedArray[self.zeroPosition + 1]
            changedArray[self.zeroPosition+1] = 0
            changedArray[self.zeroPosition] = tmp
            nextZeroPos = self.zeroPosition + 1
            return JigsawWithHeuristic(self.height, self.width, changedArray, nextZeroPos, self.path + "R", self.heuristic)

    def calculateHeuristicValue(self):
        solution = correctSolution(self.width, self.height)
        if(self.heuristic == "hamm"):  # how many tiles are not in correct place, except zero
            val = 0
            for i in range(self.height*self.width):
                if(self.actualArray[i] != solution[i] and self.actualArray[i] != 0):
                    val += 1
            return val
        if(self.heuristic == "manh"):  # how far every tile is from correct place, except zero
            val = 0
            for i in range(self.height*self.width):
                tileValue = self.actualArray[i]
                if(tileValue != 0):
                    tileX = (i % self.width)
                    tileY = math.floor(i/self.width)
                    solutionTileX = (tileValue - 1) % self.width
                    solutionTileY = math.floor((tileValue - 1) / self.width)
                    val += abs(tileX-solutionTileX) + abs(tileY-solutionTileY)
            return val
