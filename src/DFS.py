from collections import deque
from Jigsaw import *


class DFS:
    def __init__(self, solution):
        self.queue = deque()
        self.solution = solution
        self.visitedNodes = 0
        self.processedNodes = 0
        self.maxRecursion = 0

    def solve(self, jigsawToSolve, strategyLetters):
        self.queue.append(jigsawToSolve)

        while (len(self.queue) != 0):
            jigsaw = self.queue.pop()
            if len(jigsaw.path) > self.maxRecursion:
                self.maxRecursion = len(jigsaw.path)
            self.processedNodes += 1
            self.visitedNodes += 1
            if jigsaw.actualArray == self.solution:
                return jigsaw

            pathLength = len(jigsaw.path)
            if pathLength < 20:
                for i in range(4):
                    if(pathLength == 0):
                        if(strategyLetters[3-i] == "L"):
                            modifiedJigsaw = jigsaw.swapLeft()
                            if(modifiedJigsaw != None):
                                self.queue.append(modifiedJigsaw)
                                self.visitedNodes += 1
                        if(strategyLetters[3-i] == "R"):
                            modifiedJigsaw = jigsaw.swapRight()
                            if(modifiedJigsaw != None):
                                self.queue.append(modifiedJigsaw)
                                self.visitedNodes += 1
                        if(strategyLetters[3-i] == "U"):
                            modifiedJigsaw = jigsaw.swapUp()
                            if(modifiedJigsaw != None):
                                self.queue.append(modifiedJigsaw)
                                self.visitedNodes += 1
                        if(strategyLetters[3-i] == "D"):
                            modifiedJigsaw = jigsaw.swapDown()
                            if(modifiedJigsaw != None):
                                self.queue.append(modifiedJigsaw)
                                self.visitedNodes += 1
                    else:
                        if jigsaw.path[pathLength-1] != "R" and strategyLetters[3-i] == "L":
                            modifiedJigsaw = jigsaw.swapLeft()
                            if(modifiedJigsaw != None):
                                self.queue.append(modifiedJigsaw)
                                self.visitedNodes += 1
                        if jigsaw.path[pathLength-1] != "L" and strategyLetters[3-i] == "R":
                            modifiedJigsaw = jigsaw.swapRight()
                            if(modifiedJigsaw != None):
                                self.queue.append(modifiedJigsaw)
                                self.visitedNodes += 1
                        if jigsaw.path[pathLength-1] != "D" and strategyLetters[3-i] == "U":
                            modifiedJigsaw = jigsaw.swapUp()
                            if(modifiedJigsaw != None):
                                self.visitedNodes += 1
                                self.queue.append(modifiedJigsaw)
                        if jigsaw.path[pathLength-1] != "U" and strategyLetters[3-i] == "D":
                            modifiedJigsaw = jigsaw.swapDown()
                            if(modifiedJigsaw != None):
                                self.queue.append(modifiedJigsaw)
                                self.visitedNodes += 1

        return None
