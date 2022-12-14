############################################################
# IMPORT
############################################################
from Utils import *
from itertools import product
from typing import List
from typing import Tuple
import copy
import numpy as np

############################################################
# CONFIGURATION
############################################################
TEST = 0

############################################################
# DEFINITIONS
############################################################
INPUT_FILES = ["12.txt", "12.ex"]

############################################################
# METHODS
############################################################
def isValid(plan_: np.array, steps_: np.array, current_: Tuple[int,int], next_: Tuple[int,int]) -> bool:
    if (next_[0] < 0) or (next_[0] >= np.size(plan_, 0)) or (next_[1] < 0) or (next_[1] >= np.size(plan_, 1)):
        # Map edges
        return False
    if (steps_[next_] != 0):
        # nextPos already tested
        return False
    if ((plan_[next_] - plan_[current_]) > 1):
        # Delta > 1
        return False
    
    return True

def display(arr_: np.array):
    s = "\n"
    for i in range(np.size(arr_,0)):
        for j in range(np.size(arr_,1)):
            s += ' ' + str(arr_[i][j])
        s += '\n'
    
    f = open('out.log', 'w')
    f.write(s)
    f.close()

############################################################
# CLASS PUZZLE
############################################################
class Puzzle:
    filename: str
    result1: int
    result2: int
    mp: np.array
    start: Tuple[int,int]
    end = Tuple[int,int]
    
    def __init__(self, filename_: str):
        self.filename = filename_
        self.result1 = 0
        self.result2 = 1E9
        self.start = (0,0)
        self.end = (0,0)
    
    def getResult1(self) -> int:
        return self.result1

    def getResult2(self) -> int:
        return self.result2
    
    def loadPlan(self):
        lines = readLines(self.filename)
        
        self.mp = np.zeros((len(lines), len(lines[0])), dtype = int)
        
        for x,y in product(range(np.size(self.mp,0)), range(np.size(self.mp,1))):
            if (lines[x][y] == 'S'):
                self.start = (x,y)
                self.mp[x,y] = 0
            elif (lines[x][y] == 'E'):
                self.end = (x,y)
                self.mp[x,y] = 25
            else:
                self.mp[x,y] = ord(lines[x][y]) - ord('a')

    
    def searchPath(self, start_: Tuple[int,int]) -> int:
        path = [start_]
        
        steps = np.zeros((np.size(self.mp,0),np.size(self.mp,1)), dtype = int)
        steps[start_] = 0
        
        dtPos = [(-1,0), (1,0), (0,-1), (0,1)]
        
        while (len(path) != 0):
            current = path[0]
            path = path[1:]
            
            for pos in dtPos:
                nextPos = tuple(map(lambda x,y: x+y, current, pos))
                if isValid(self.mp, steps, current, nextPos):
                    steps[nextPos] = steps[current] + 1
                    path.append(nextPos)

        return steps[self.end]                
        
    def run(self):
        self.loadPlan()

        # Part 1
        self.result1 = self.searchPath(self.start)
        
        # Part 2
        starts = []
        for x,y in product(range(np.size(self.mp,0)), range(np.size(self.mp,1))):
            if (self.mp[x,y] == 0):
                starts.append((x,y))
                
        for start in starts:
            result = self.searchPath(start)
            
            if ((result != 0) and (result < self.result2)):
                self.result2 = result

        return            

############################################################
# MAIN
############################################################
filename = "data/" + INPUT_FILES[TEST]
p = Puzzle(filename)
p.run()
print("Result 1: " + str(p.getResult1()))
print("Result 2: " + str(p.getResult2()))