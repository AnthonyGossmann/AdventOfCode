############################################################
# IMPORT
############################################################
from Utils import *
import typing
from typing import Tuple
import numpy as np

############################################################
# CONFIGURATION
############################################################
TEST = 0

############################################################
# DEFINITIONS
############################################################
INPUT_FILES = ["14.txt", "14.ex"]

############################################################
# CLASS PUZZLE
############################################################
class Puzzle:
    filename: str
    result1: int
    result2: int
    grid: np.array
    width: int
    depth: int
    offset: int
    center: Tuple[int,int]
    
    def __init__(self, filename_: str):
        self.filename = filename_
        self.result1 = 0
        self.result2 = 0
        self.width = 0
        self.depth = 0
        self.offset = 0
        self.center = (0,0)

    def getResult1(self):
        return self.result1

    def getResult2(self):
        return self.result2            
    
    def loadGrid(self, part2_: bool = False):
        lines = readLines(self.filename)
        
        # Get grid size
        left = 500
        right = 500
        depth = 0
        
        for line in lines:
            for token in line.split(" -> "):
                p = eval(token)
                if (p[0] > right):
                    right = p[0]
                if (p[0] < left):
                    left = p[0]
                if (p[1] > depth):
                    depth = p[1]
        
        if part2_:
            self.depth = (depth + 1) + 2
            self.width = (right - left) + 1 + 2 * (self.depth - 1)
            self.offset = left - (self.depth - 1)     
        else:
            self.depth = (depth + 1)
            self.width = (right - left) + 1
            self.offset = left
    
        self.center = (0, 500 - self.offset)
        self.grid = np.zeros((self.depth,self.width), dtype=int)   
        
        # Fill grid
        for line in lines:
            tokens = line.split(" -> ")
            for i in range(1,len(tokens)):
                p1 = eval(tokens[i-1])
                p2 = eval(tokens[i])
                
                if (p1[0] == p2[0]):
                    for j in range(min(p1[1],p2[1]), max(p1[1],p2[1])+1):
                        self.grid[(j,p1[0]-self.offset)] = -1
                elif (p1[1] == p2[1]):
                    for j in range(min(p1[0],p2[0]), max(p1[0],p2[0])+1):
                        self.grid[(p1[1],j-self.offset)] = -1    
                        
        # Part 2
        if part2_:
            for i in range(self.width):
                self.grid[(self.depth-1,i)] = -1                
    
    def fall(self, pos_: Tuple[int,int], part2_: bool = False) -> bool:
        ret = False

        cur = pos_
        while True:
            # Down
            nPos = (cur[0] + 1, cur[1])
            if (nPos[0] >= np.size(self.grid,0)):
                ret = True
                break
            
            if (self.grid[nPos] == 0):
                cur = nPos
                continue
            
            # Down left
            nPos = (cur[0] + 1, cur[1] - 1)
            if (nPos[1] < 0):
                if not part2_:
                    ret = True
                break
            
            if (self.grid[nPos] == 0):
                cur = nPos
                continue
            
            # Down right
            nPos = (cur[0] + 1, cur[1] + 1)
            if (nPos[1] >= np.size(self.grid,1)):
                if not part2_:
                    ret = True
                break
            
            if (self.grid[nPos] == 0):
                cur = nPos
                continue

            break
            
        if not ret:
            self.grid[cur] = 1
            if (part2_ and (self.grid[self.center] == 1)):
                ret = True

        return ret

    def run(self):
        # Part 1
        self.loadGrid()

        ret = False
        while not ret:
            ret = self.fall(self.center)
            if not ret:
                self.result1 += 1
    
        # Part 2
        self.loadGrid(True)

        ret = False
        while not ret:
            ret = self.fall(self.center, True)
            if not ret:
                self.result2 += 1
        self.result2 += 1
        
############################################################
# MAIN
############################################################
filename = "data/" + INPUT_FILES[TEST]
p = Puzzle(filename)
p.run()
print("Result 1: " + str(p.getResult1()))
print("Result 2: " + str(p.getResult2()))   