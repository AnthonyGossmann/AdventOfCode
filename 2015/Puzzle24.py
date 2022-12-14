############################################################
# IMPORT
############################################################
from Utils import *
from itertools import combinations
import math

############################################################
# CONFIGURATION
############################################################
TEST = 0

############################################################
# DEFINITIONS
############################################################
INPUT_FILES = ["24.txt", "24.ex"]

############################################################
# CLASS PUZZLLE
############################################################
class Puzzle:
    filename: str
    result1: int
    result2: int
    pkgs: List[int]
    
    def __init__(self, filename_: str):
        self.filename = filename_
        self.result1 = 0
        self.result2 = 0
        self.pkgs = []
    
    def getResult1(self) -> int:
        return self.result1

    def getResult2(self) -> int:
        return self.result2

    def loadPkgs(self):
        lines = readLines(self.filename)
        for line in lines:
            self.pkgs.append(int(line))
            
    def findQE(self, n: int = 3):
        moyGrp = sum(self.pkgs) // n
        minGrp = min(i for i in range(1,len(self.pkgs)) if sum(self.pkgs[-i:]) >= moyGrp)

        groups = []
        for i in range(minGrp, len(self.pkgs) // n + 1):
            for c in combinations(self.pkgs, i):
                if (sum(c) == moyGrp):
                    groups.append(c)
           
        qe = [math.prod(i) for i in groups]

        return min(qe)

    def run(self):
        self.loadPkgs()
        
        # Part 1
        self.result1 =  self.findQE()
        
        # Part 2
        self.result2 =  self.findQE(4)
        
    
############################################################
# MAIN
############################################################
filename = "data/" + INPUT_FILES[TEST]
p = Puzzle(filename)
p.run()
print("Result 1: " + str(p.getResult1()))
print("Result 2: " + str(p.getResult2()))              
