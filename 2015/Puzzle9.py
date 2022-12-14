############################################################
# IMPORT
############################################################
from Utils import *
from typing import List
from itertools import permutations

############################################################
# CONFIGURATION
############################################################
TEST = 0

############################################################
# DEFINITIONS
############################################################
INPUT_FILES = ["09.txt", "09.ex"]

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
        self.result1 = 1E9
        self.result2 = 0
    
    def getResult1(self) -> int:
        return self.result1

    def getResult2(self) -> int:
        return self.result2

    def run(self):
        lines = readLines(self.filename)
        
        cities = set()
        distances = dict()

        for line in lines:
            found = re.fullmatch("(.+) to (.+) = (\d+)", line)
            cities.add(found.group(1))
            cities.add(found.group(2))
            
            distances.setdefault(found.group(1), dict())[found.group(2)] = int(found.group(3))
            distances.setdefault(found.group(2), dict())[found.group(1)] = int(found.group(3))
        
        for path in permutations(cities):
            distance = sum([distances[path[i]][path[i+1]] for i in range(0, len(path) - 1)])
            self.result1 = min(self.result1, distance)
            self.result2 = max(self.result2, distance)
            
############################################################
# MAIN
############################################################
filename = "data/" + INPUT_FILES[TEST]
p = Puzzle(filename)
p.run()
print("Result 1: " + str(p.getResult1()))
print("Result 2: " + str(p.getResult2()))          
