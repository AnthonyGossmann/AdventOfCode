############################################################
# Import
############################################################
from Utils import *
from itertools import combinations
from collections import Counter

############################################################
# Class Puzzle17
############################################################
class Puzzle17:
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
        containers = apply(int, readLines(self.filename))
        target = 150

        # Part 1
        results = Counter()
        for i in range(len(containers)):
            for c in combinations(containers, i):
                if (sum(c) == target):
                    self.result1 += 1
                    results[i] += 1
        # Part 2
        self.result2 = results[min(results)]
               
        return            
