############################################################
# IMPORT
############################################################
from Utils import *
from itertools import product

############################################################
# CONFIGURATION
############################################################
TEST = 0

############################################################
# DEFINITIONS
############################################################
INPUT_FILES = ["25.txt", "25.ex"]

############################################################
# METHODS
############################################################
def findStep(code_: int) -> int:
    pos = [1,1]
    x = 1
    step = 1
    
    while (pos != code_):
        if (pos[0] == 1):
            x += 1
            pos[0] = x
            pos[1] = 1
        else:
            pos[0] -= 1
            pos[1] += 1

        step += 1
    
    return step
    
def computeCode(step_: int) -> int:
    code = 20151125
    for i in range(step_-1):
        code *= 252533
        code %= 33554393
        
    return code

############################################################
# CLASS PUZZLE
############################################################
class Puzzle:
    filename: str
    result1: int
    result2: int
    code: List
    
    def __init__(self, filename_: str):
        self.filename = filename_
        self.result1 = 0
        self.result2 = 0
        self.code = []
    
    def getResult1(self) -> int:
        return self.result1

    def getResult2(self) -> int:
        return self.result2
    
    def loadCode(self) -> int:
        text = readFile(self.filename)
        found = re.fullmatch("To continue, please consult the code grid in the manual.  Enter the code at row (.+), column (.+).", text)
        code = [int(found.group(1)), int(found.group(2))]
        return code

    def run(self):
        code = self.loadCode()
        step = findStep(code)
        self.result1 = computeCode(step)
        
    
############################################################
# MAIN
############################################################
filename = "data/" + INPUT_FILES[TEST]
p = Puzzle(filename)
p.run()
print("Result 1: " + str(p.getResult1()))
#print("Result 2: " + str(p.getResult2()))               
