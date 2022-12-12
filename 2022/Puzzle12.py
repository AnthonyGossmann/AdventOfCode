############################################################
# Import
############################################################
from Utils import *
from itertools import product
from typing import List
from typing import Tuple
import copy
import numpy as np

############################################################
# Static Methods
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
# Class Puzzle12
############################################################
class Puzzle12:
    filename: str
    result1: int
    result2: int
    
    def __init__(self, filename_):
        self.filename = filename_
        self.result1 = 0
        self.result2 = 1E9
    
    def getResult1(self) -> int:
        return self.result1

    def getResult2(self) -> int:
        return self.result2
    
    def loadPlan(self, lines_: List[str]) -> [np.array, Tuple[int,int], Tuple[int,int]]:
        plan = np.zeros((len(lines_), len(lines_[0])), dtype = int)
        start = (-1,-1)
        end = (-1,-1)
        
        for x,y in product(range(np.size(plan,0)), range(np.size(plan,1))):
            if (lines_[x][y] == 'S'):
                start = (x,y)
                plan[x,y] = 0
            elif (lines_[x][y] == 'E'):
                end = (x,y)
                plan[x,y] = 25
            else:
                plan[x,y] = ord(lines_[x][y]) - ord('a')
            
        return [plan, start, end]
    
    def searchPath(self, plan_: np.array, start_: Tuple[int,int], end_: Tuple[int,int]) -> int:
        path = [start_]
        
        steps = np.zeros((np.size(plan_,0),np.size(plan_,1)), dtype = int)
        steps[start_] = 0
        
        dtPos = [(-1,0), (1,0), (0,-1), (0,1)]
        
        while (len(path) != 0):
            current = path[0]
            path = path[1:]
            
            for pos in dtPos:
                nextPos = tuple(map(lambda x,y: x+y, current, pos))
                if isValid(plan_, steps, current, nextPos):
                    steps[nextPos] = steps[current] + 1
                    path.append(nextPos)

        return steps[end_]                
        
    def run(self):
        lines = readLines(self.filename)
        [plan, start, end] = self.loadPlan(lines)

        # Part 1
        self.result1 = self.searchPath(plan, start, end)
        
        # Part 2
        starts = []
        for x,y in product(range(np.size(plan,0)), range(np.size(plan,1))):
            if (plan[x,y] == 0):
                starts.append((x,y))
                
        for start in starts:
            result = self.searchPath(plan, start, end)
            
            if ((result != 0) and (result < self.result2)):
                self.result2 = result

        return            
