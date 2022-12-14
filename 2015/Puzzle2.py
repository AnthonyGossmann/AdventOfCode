############################################################
# IMPORT
############################################################
from Utils import *
import re
import math

############################################################
# CONFIGURATION
############################################################
TEST = 0

############################################################
# DEFINITIONS
############################################################
INPUT_FILES = ["02.txt", "02.ex"]

############################################################
# METHODS
############################################################

############################################################
# CLASS PUZZLE
############################################################
class Puzzle:
    filename: str
    result1: int
    result2: int
    
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
        
        boxes = []
        for line in lines:
            found = re.fullmatch("(.+)x(.+)x(.+)", line)
            box = [int(found.group(i)) for i in range(1,4)]
            box.sort()
            
            self.result1 += 3 * box[0] * box[1] + 2 * box[1] * box[2] + 2 * box[0] * box[2]
            self.result2 += 2 * (box[0] + box[1]) + math.prod(box)

############################################################
# MAIN
############################################################
filename = "data/" + INPUT_FILES[TEST]
p = Puzzle(filename)
p.run()
print("Result 1: " + str(p.getResult1()))
print("Result 2: " + str(p.getResult2()))         
