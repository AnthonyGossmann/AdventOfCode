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
INPUT_FILES = ["03.txt", "03.ex"]

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
        offsetLower = ord('a') - 1
        offsetUpper = ord('A') - 1 - 26
   
        # Part 1
        for line in lines:
            item1 = line[:(int)(len(line)/2)]
            item2 = line[(int)(len(line)/2):]
            matches = set(item1).intersection(item2)
        
            for m in matches:
                p = (ord(m) - offsetUpper) if m.isupper() else (ord(m) - offsetLower)
                self.result1 += p
                
        # Part 2
        for i in range(0, len(lines) - 2, 3):
            matches = set(lines[i]).intersection(lines[i+1]).intersection(lines[i+2])
            
            for m in matches:
                p = (ord(m) - offsetUpper) if m.isupper() else (ord(m) - offsetLower)
                self.result2 += p            

############################################################
# MAIN
############################################################
filename = "data/" + INPUT_FILES[TEST]
p = Puzzle(filename)
p.run()
print("Result 1: " + str(p.getResult1()))
print("Result 2: " + str(p.getResult2()))