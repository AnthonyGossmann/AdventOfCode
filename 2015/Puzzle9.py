############################################################
# Import
############################################################
from Utils import *
from typing import List
from itertools import permutations

############################################################
# Class Puzzle9
############################################################
class Puzzle9:
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
        
        cities = []
        data = {}
        for line in lines:
            found = re.fullmatch("(.+) to (.+) = (\d+)", line)
            if (found.group(1) not in cities):
                cities.append(found.group(1))
            if (found.group(2) not in cities):
                cities.append(found.group(2))
            data[found.group(1) + "_" + found.group(2)] = int(found.group(3))
            data[found.group(2) + "_" + found.group(1)] = int(found.group(3))
    
        dist = []
        for path in permutations(cities):
            d = 0
            for i in range(0, len(path) - 1):
                d += data[path[i] + "_" + path[i+1]]
            dist.append(d)
            
        self.result1 = min(dist)
        self.result2 = max(dist)
            
        return            
