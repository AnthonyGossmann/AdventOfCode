############################################################
# Import
############################################################
from Utils import *
from itertools import permutations

############################################################
# Class Puzzle17
############################################################
class Puzzle17:
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
        results = []
        for i in range(0, 2**(len(containers))):
            total = 0
            j = 0
            cnt = 0
            while ((j < len(containers)) and (total <= target)):
                if (i & (1 << j)):
                    total += containers[j]
                    cnt += 1
                j += 1
            
            if (total == target):
                self.result1 += 1
                results.append(cnt)
      
        # Part 2
        self.result2 = results.count(min(results))
               
      
        return            
