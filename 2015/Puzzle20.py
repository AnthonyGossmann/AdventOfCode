############################################################
# IMPORT
############################################################
from Utils import *
from typing import *
from sympy.ntheory import factorint
import numpy as np

############################################################
# CONFIGURATION
############################################################
TEST = 0

############################################################
# DEFINITIONS
############################################################
INPUT_FILES = ["20.txt", "20.ex"]

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
        target = int(readFile(self.filename))
        
        # Part 1
        while True:
            self.result1 += 1
            factors = factorint(self.result1)
            results = np.ones(1, dtype=int)
            
            for prime, power in factors.items():
                results = np.outer(np.array([prime ** k for k in range(power + 1)]), results).ravel()
            
            if (sum(results) * 10 >= target):
                break
        
        # Part 2
        while True:
            self.result2 += 1
            factors = []
        
            for i in range(1, 51):
                if ((self.result2 / i) == (self.result2 // i)):
                    factors.append(self.result2 // i)
            
            if (sum(factors) * 11 >= target):
                break    

############################################################
# MAIN
############################################################
filename = "data/" + INPUT_FILES[TEST]
p = Puzzle(filename)
p.run()
print("Result 1: " + str(p.getResult1()))
print("Result 2: " + str(p.getResult2()))            
