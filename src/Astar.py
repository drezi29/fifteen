from JigsawWithHeuristic import *
from Jigsaw import *


class Astar:
    def __init__(self, solution):
        self.states = []
        self.solution = solution
        self.visitedNodes = 0
        self.processedNodes = 0
        self.maxRecursion = 0

    def solve(self, jigsawToSolve):
        self.states.append(jigsawToSolve)
        goalState = self.solution
        while(len(self.states) != 0):
            startState = self.states[0]
            self.states.pop(0)
            self.processedNodes += 1
            self.visitedNodes += 1
            if len(startState.path) > self.maxRecursion:
                self.maxRecursion = len(startState.path)
            if(startState.actualArray == goalState):
                return startState

            if(len(startState.path) == 0):
                tmp = startState.swapLeft()
                if(tmp != None):
                    self.states.append(tmp)
                    self.visitedNodes += 1
                tmp = startState.swapRight()
                if(tmp != None):
                    self.states.append(tmp)
                    self.visitedNodes += 1
                tmp = startState.swapUp()
                if(tmp != None):
                    self.states.append(tmp)
                    self.visitedNodes += 1
                tmp = startState.swapDown()
                if(tmp != None):
                    self.states.append(tmp)
                    self.visitedNodes += 1
            elif(len(startState.path) < 20):
                if(startState.path[len(startState.path)-1] != "R"):
                    tmp = startState.swapLeft()
                    if(tmp != None):
                        self.states.append(tmp)
                        self.visitedNodes += 1
                if(startState.path[len(startState.path)-1] != "L"):
                    tmp = startState.swapRight()
                    if(tmp != None):
                        self.states.append(tmp)
                        self.visitedNodes += 1
                if(startState.path[len(startState.path)-1] != "D"):
                    tmp = startState.swapUp()
                    if(tmp != None):
                        self.states.append(tmp)
                        self.visitedNodes += 1
                if(startState.path[len(startState.path)-1] != "U"):
                    tmp = startState.swapDown()
                    if(tmp != None):
                        self.states.append(tmp)
                        self.visitedNodes += 1

            self.states.sort(key=lambda x: x.heuristicValue, reverse=False)
        return None
