############################################################
# IMPORT
############################################################
from Utils import *
import numpy as np
from itertools import product

############################################################
# CONFIGURATION
############################################################
TEST = 0

############################################################
# DEFINITIONS
############################################################
INPUT_FILES = ["08.txt", "08.ex"]

############################################################
# METHODS
############################################################
def isVisible(trees_: np.array, x_: int, y_: int) -> bool:
    if ((x_ == 0) or (x_ == len(trees_)-1) or (y_ == 0) or (y_ == len(trees_[0])-1)):
        return True
    
    # Top
    b1 = (trees_[x_,y_] > max(trees_[:x_,y_]))
    # Bottom
    b2 = (trees_[x_,y_] > max(trees_[x_+1:,y_]))
    # Left
    b3 = (trees_[x_,y_] > max(trees_[x_,:y_]))
    # Right
    b4 = (trees_[x_,y_] > max(trees_[x_,y_+1:]))

    return (b1 or b2 or b3 or b4)

def distance(trees_: np.array, x_: int, y_: int) -> int:
    if ((x_ == 0) or (x_ == len(trees_)-1) or (y_ == 0) or (y_ == len(trees_[0])-1)):
        return 0
    
    # Top
    s1 = 0
    for i in range(x_-1, -1, -1):
        s1 += 1
        if (trees_[i,y_] >= trees_[x_,y_]):
            break

    # Bottom
    s2 = 0
    for i in range(x_+1, len(trees_), 1):
        s2 += 1
        if (trees_[i,y_] >= trees_[x_,y_]):
            break

    # Left
    s3 = 0
    for i in range(y_-1, -1, -1):
        s3 += 1
        if (trees_[x_,i] >= trees_[x_,y_]):
            break
    
    # Right
    s4 = 0
    for i in range(y_+1, len(trees_[0]) , 1):
        s4 += 1
        if (trees_[x_,i] >= trees_[x_,y_]):
            break
    
    return s1 * s2 * s3 * s4

############################################################
# CLASS PUZZLE
############################################################
class Puzzle:
    filename: str
    result1: int
    reuslt2: int
    
    def __init__(self, filename_: str):
        self.filename = filename_
        self.result1 = 0
        self.result2 = 0
    
    def getResult1(self) -> int:
        return self.result1

    def getResult2(self) -> int:
        return self.result2

    def run(self):
        lines = readLines(self.filename)
        length = len(lines)
        width = len(lines[0])
        
        trees = np.zeros((length, width), dtype=int)
        for i,j in product(range(length), range(width)):
            trees[i][j] = int(lines[i][j])
            
        # Part 1
        for i,j in product(range(length), range(width)):
            if isVisible(trees, i, j):
                self.result1 += 1

        # Part 2
        for i,j in product(range(length), range(width)):
            score = distance(trees, i, j)
            self.result2 = max(self.result2, score)

############################################################
# MAIN
############################################################
filename = "data/" + INPUT_FILES[TEST]
p = Puzzle(filename)
p.run()
print("Result 1: " + str(p.getResult1()))
print("Result 2: " + str(p.getResult2()))
