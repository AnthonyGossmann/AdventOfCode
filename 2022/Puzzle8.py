############################################################
# Import
############################################################
from Utils import *
import numpy as np
from itertools import product

############################################################
# Static Methods
############################################################
def isVisible(trees_, x_: int, y_: int) -> bool:
    if ((x_ == 1) or (x_ == len(trees_) - 2) or (y_ == 1) or (y_ == len(trees_[0]) - 2)):
        return True
    
    # Top
    b1 = (trees_[x_,y_] > max(trees_[0:x_,y_]))
    # Bottom
    b2 = (trees_[x_,y_] > max(trees_[x_+1:,y_]))
    # Left
    b3 = (trees_[x_,y_] > max(trees_[x_,0:y_]))
    # Right
    b4 = (trees_[x_,y_] > max(trees_[x_,y_+1:]))

    return (b1 or b2 or b3 or b4)

def distance(trees_, x_: int, y_: int) -> int:
    if ((x_ == 1) or (x_ == len(trees_) - 2) or (y_ == 1) or (y_ == len(trees_[0]) - 2)):
        return 0
    
    # Top
    s1 = 0
    for i in range(x_-1, 0, -1):
        s1 += 1
        if (trees_[i,y_] >= trees_[x_,y_]):
            break

    # Bottom
    s2 = 0
    for i in range(x_+1, len(trees_)-1, 1):
        s2 += 1
        if (trees_[i,y_] >= trees_[x_,y_]):
            break

    # Left
    s3 = 0
    for i in range(y_-1, 0, -1):
        s3 += 1
        if (trees_[x_,i] >= trees_[x_,y_]):
            break
    
    # Right
    s4 = 0
    for i in range(y_+1, len(trees_[0])-1 , 1):
        s4 += 1
        if (trees_[x_,i] >= trees_[x_,y_]):
            break
    
    return s1 * s2 * s3 * s4

############################################################
# Class Puzzle8
############################################################
class Puzzle8:
    def __init__(self, filename_):
        self.filename:str = filename_
        self.result1: int = 0
        self.result2: int = 0
    
    def getResult1(self) -> int:
        return self.result1

    def getResult2(self) -> int:
        return self.result2

    def run(self):
        lines = readLines(self.filename)
        length = len(lines)
        width = len(lines[0])
        
        trees = np.zeros((length + 2, width + 2))
        trees.astype(int)
        for i,j in product(range(length + 2), range(width + 2)):
            if ((i == 0) or (i == length + 1) or (j == 0) or (j == width + 1)):
                trees[i][j] = int(0)
            else:
                trees[i][j] = int(lines[i - 1][j - 1])
            
        # Part 1
        for i,j in product(range(1, length + 1), range(1, width + 1)):
            if isVisible(trees, i, j):
                self.result1 += 1

        # Part 2
        for i,j in product(range(1, length + 1), range(1, width + 1)):
            score = distance(trees, i, j)
            self.result2 = max(self.result2, score)
        
        return            
