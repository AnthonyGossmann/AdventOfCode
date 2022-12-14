############################################################
# IMPORT
############################################################
from Utils import *
import re

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
def score(p1_: int, p2_: int) -> int:
    if ((p2_ == 3) and (p1_ == 1)):
        return p2_
    elif (((p2_ == 1) and (p1_ == 3)) or (p2_ > p1_)):
        return p2_ + 6
    elif (p2_ == p1_):
        return p2_ + 3
    return p2_

def scoreFromOutcome(p1_: int, out_: int) -> int:
    if (out_ == 1):
        return (3 if (p1_ == 1) else (p1_ - 1))
    elif (out_ == 2):
        return p1_ + 3
    else:
        return (1 if (p1_ == 3) else (p1_ + 1)) + 6

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
        text = re.sub("[AX]", "1", text)
        text = re.sub("[BY]", "2", text)
        text = re.sub("[CZ]", "3", text)    
        rounds = apply(int, re.split("[ \n]", text))

        for i in range(0, len(rounds) - 1, 2):
            self.result1 += score(rounds[i], rounds[i+1])
            self.result2 += scoreFromOutcome(rounds[i], rounds[i+1])       

############################################################
# MAIN
############################################################
filename = "data/" + INPUT_FILES[TEST]
p = Puzzle(filename)
p.run()
print("Result 1: " + str(p.getResult1()))
print("Result 2: " + str(p.getResult2()))