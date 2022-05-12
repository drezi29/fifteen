from collections import deque
from Jigsaw import *


class BFS:
    def __init__(self, solution):
        self.queue = deque()
        self.solution = solution
        self.visitedNodes = 0
        self.processedNodes = 0
        self.maxRecursion = 0

    def solve(self, jigsawToSolve, strategyLetters):
        self.queue.append(jigsawToSolve)

        while (len(self.queue) != 0):
            jigsaw = self.queue.popleft()
            if len(jigsaw.path) > self.maxRecursion:
                self.maxRecursion = len(jigsaw.path)
            self.visitedNodes += 1
            self.processedNodes += 1
            if jigsaw.actualArray == self.solution:
                return jigsaw

            pathLength = len(jigsaw.path)
            if pathLength < 20:
                for i in range(4):
                    if(pathLength == 0):
                        if(strategyLetters[i] == "L"):
                            modifiedJigsaw = jigsaw.swapLeft()
                            if(modifiedJigsaw != None):
                                self.queue.append(modifiedJigsaw)
                                self.visitedNodes += 1
                        if(strategyLetters[i] == "R"):
                            modifiedJigsaw = jigsaw.swapRight()
                            if(modifiedJigsaw != None):
                                self.queue.append(modifiedJigsaw)
                                self.visitedNodes += 1
                        if(strategyLetters[i] == "U"):
                            modifiedJigsaw = jigsaw.swapUp()
                            if(modifiedJigsaw != None):
                                self.queue.append(modifiedJigsaw)
                                self.visitedNodes += 1
                        if(strategyLetters[i] == "D"):
                            modifiedJigsaw = jigsaw.swapDown()
                            if(modifiedJigsaw != None):
                                self.queue.append(modifiedJigsaw)
                                self.visitedNodes += 1
                    else:
                        if jigsaw.path[pathLength-1] != "R" and strategyLetters[i] == "L":
                            modifiedJigsaw = jigsaw.swapLeft()
                            if(modifiedJigsaw != None):
                                self.queue.append(modifiedJigsaw)
                                self.visitedNodes += 1
                        if jigsaw.path[pathLength-1] != "L" and strategyLetters[i] == "R":
                            modifiedJigsaw = jigsaw.swapRight()
                            if(modifiedJigsaw != None):
                                self.queue.append(modifiedJigsaw)
                                self.visitedNodes += 1
                        if jigsaw.path[pathLength-1] != "D" and strategyLetters[i] == "U":
                            modifiedJigsaw = jigsaw.swapUp()
                            if(modifiedJigsaw != None):
                                self.queue.append(modifiedJigsaw)
                                self.visitedNodes += 1
                        if jigsaw.path[pathLength-1] != "U" and strategyLetters[i] == "D":
                            modifiedJigsaw = jigsaw.swapDown()
                            if(modifiedJigsaw != None):
                                self.queue.append(modifiedJigsaw)
                                self.visitedNodes += 1

        return None
