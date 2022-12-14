############################################################
# IMPORT
############################################################
from Utils import *

############################################################
# CONFIGURATION
############################################################
TEST = 0

############################################################
# DEFINITIONS
############################################################
INPUT_FILES = ["06.txt", "06.ex"]

############################################################
# METHODS
############################################################
def findMarker(text_: str, length_: int) -> int:
    for i in range(len(text_) - length_ + 1):
        sub = list(set(text_[i:i+length_]))
        if (len(sub) == length_):
            return i + length_

    return -1

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
        text = readFile(self.filename)    

        self.result1 = findMarker(text, 4)
        self.result2 = findMarker(text, 14)

############################################################
# MAIN
############################################################
filename = "data/" + INPUT_FILES[TEST]
p = Puzzle(filename)
p.run()
print("Result 1: " + str(p.getResult1()))
print("Result 2: " + str(p.getResult2()))
