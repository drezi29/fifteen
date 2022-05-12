import sys
from JigsawReader import *
from JigsawWithHeuristic import *
from Jigsaw import *
from BFS import *
from DFS import *
from Astar import *
import timeit

# How to run - examples:
# BFS -> python -u main.py bfs LUDR jigsaw.txt solution.txt information.txt
# DFS -> python -u main.py dfs LUDR j.txt s.txt i.txt
# Astar -> python -u main.py astr manh j.txt. s.txt i.txt
# Astar -> python -u main.py astr hamm j.txt s.txt i.txt

lettersPermutation = ["LRUD", "LRDU", "LURD", "LUDR", "LDRU", "LDUR",
                      "RLUD", "RLDU", "RULD", "RUDL", "RDLU", "RDUL",
                      "URLD", "URDL", "UDRL", "UDLR", "ULDR", "ULRD",
                      "DURL", "DULR", "DRUL", "DRLU", "DLUR", "DLRU"]
falsePermutation = 0


if len(sys.argv) != 6:
    print("Specify all program call parameters")
    exit(0)

strategy = sys.argv[1]
parameterOfStrategy = sys.argv[2]
startFifteenFile = sys.argv[3]
solutionFifteenFile = sys.argv[4]
calculationInformationFile = sys.argv[5]

if len(sys.argv) == 6:
    if(strategy != "bfs" and strategy != "dfs" and strategy != "astr"):
        print("The selected strategy does not exist, available strategies: bfs, dfs, astr")
        exit(0)
    if(strategy == "bfs" or strategy == "dfs"):
        for permutation in lettersPermutation:
            if(parameterOfStrategy != permutation):
                falsePermutation = falsePermutation+1
        if falsePermutation == 24:
            print(
                "The selected strategy parameter does not exist (parameter should be a permutation of these letters: LRDU)")
            exit(0)
    if(strategy == "astr"):
        if(parameterOfStrategy != "manh" and parameterOfStrategy != "hamm"):
            print(
                "The selected strategy parameter does not exist, available parameters: hamm, manh")
            exit(0)

myJigsawFileReader = jigsawReader(f"{startFifteenFile}")
parsedJigsawFromFile = myJigsawFileReader.jigsaw
correctGeneratedSolution = correctSolution(
    myJigsawFileReader.width, myJigsawFileReader.height)

if strategy == "bfs" or strategy == "dfs":
    startJigsaw = Jigsaw(myJigsawFileReader.height,
                         myJigsawFileReader.width, parsedJigsawFromFile, None, "")
    if strategy == "bfs":
        starttime = timeit.default_timer()
        bfsSolver = BFS(correctGeneratedSolution)
        solution = bfsSolver.solve(startJigsaw, parameterOfStrategy)
        fullTime = timeit.default_timer() - starttime

    if strategy == "dfs":
        starttime = timeit.default_timer()
        dfsSolver = DFS(correctGeneratedSolution)
        solution = dfsSolver.solve(startJigsaw, parameterOfStrategy)
        fullTime = timeit.default_timer() - starttime

if strategy == "astr":
    startJigsaw = JigsawWithHeuristic(
        myJigsawFileReader.height, myJigsawFileReader.width, parsedJigsawFromFile, None, "", parameterOfStrategy)

    starttime = timeit.default_timer()
    astrSolver = Astar(correctGeneratedSolution)
    solution = astrSolver.solve(startJigsaw)
    fullTime = timeit.default_timer() - starttime

fileWithSolution = open(solutionFifteenFile, "w")
if solution != None:
    fileWithSolution.write(str(len(solution.path)) + "\n" + str(solution.path))
else:
    fileWithSolution.write(-1)

fileWithInformation = open(calculationInformationFile, "w")
miliTime = fullTime * 1000
calculatingTime = round(miliTime, 3)

# CALCULATING TIME TO FILE
if strategy == "astr":
    if solution != None:
        fileWithInformation.write(str(len(solution.path)) +
                                  "\n" + str(astrSolver.visitedNodes) + "\n" + str(astrSolver.processedNodes) +
                                  "\n" + str(astrSolver.maxRecursion) + "\n" + str(calculatingTime))
    else:
        fileWithInformation.write(str(-1) +
                                  "\n" + str(astrSolver.visitedNodes) + "\n" + str(astrSolver.processedNodes) +
                                  "\n" + str(astrSolver.maxRecursion) + "\n" + str(calculatingTime))
if strategy == "bfs":
    if solution != None:
        fileWithInformation.write(str(len(solution.path)) +
                                  "\n" + str(bfsSolver.visitedNodes) + "\n" + str(bfsSolver.processedNodes) +
                                  "\n" + str(bfsSolver.maxRecursion) + "\n" + str(calculatingTime))
    else:
        fileWithInformation.write(str(-1) +
                                  "\n" + str(bfsSolver.visitedNodes) + "\n" + str(bfsSolver.processedNodes) +
                                  "\n" + str(bfsSolver.maxRecursion) + "\n" + str(calculatingTime))
if strategy == "dfs":
    if solution != None:
        fileWithInformation.write(str(len(solution.path)) +
                                  "\n" + str(dfsSolver.visitedNodes) + "\n" + str(dfsSolver.processedNodes) +
                                  "\n" + str(dfsSolver.maxRecursion) + "\n" + str(calculatingTime))
    else:
        fileWithInformation.write(str(-1) +
                                  "\n" + str(dfsSolver.visitedNodes) + "\n" + str(dfsSolver.processedNodes) +
                                  "\n" + str(dfsSolver.maxRecursion) + "\n" + str(calculatingTime))
