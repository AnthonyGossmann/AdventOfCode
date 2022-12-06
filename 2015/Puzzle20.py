############################################################
# Import
############################################################
from Utils import *
from typing import *
from sympy.ntheory import factorint
import numpy as np

############################################################
# Static Methods
############################################################
def findFactors(num_: int) -> List[int]:
    result = []
    for i in range(1, num_ + 1):
        if ((num_ % i) == 0):
            result.append(i)
    return result   

############################################################
# Class Puzzle20
############################################################
class Puzzle20:
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
        
        print(factorint(target))
        
        # Part 1
        while True:
            self.result1 += 1
            factorisation = factorint(self.result1)
            factors = np.ones(1, dtype=int)
            
            for prime, power in factorisation.items():
                factors = np.outer(np.array([prime ** k for k in range(power + 1)]), factors).ravel()
            
            if (sum(factors) * 10 >= target):
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
        


        return            
