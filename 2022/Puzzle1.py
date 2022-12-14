############################################################
# IMPORT
############################################################
from Utils import *

############################################################
# CONFIGURATION
############################################################
TEST = 1

############################################################
# DEFINITIONS
############################################################
INPUT_FILES = ["01.txt", "01.ex"]

############################################################
# METHODS
############################################################

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
        data = []
        
        current = 0
        for line in lines:
            if (len(line) == 0):
                data.append(current)
                current = 0
            else:
                current += int(line)
        data.append(current)
        data = sorted(data)
        
        self.result1 = data[-1]
        self.result2 = sum(data[-3:])       

############################################################
# MAIN
############################################################
filename = "data/" + INPUT_FILES[TEST]
p = Puzzle(filename)
p.run()
print("Result 1: " + str(p.getResult1()))
print("Result 2: " + str(p.getResult2()))