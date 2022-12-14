############################################################
# IMPORT
############################################################
from Utils import *
from typing import Dict
from typing import List
from itertools import permutations

############################################################
# CONFIGURATION
############################################################
TEST = 0

############################################################
# DEFINITIONS
############################################################
INPUT_FILES = ["13.txt", "13.ex"]

############################################################
# METHODS
############################################################
def computeHappiness(data_: Dict[str,Dict[str, int]], path_: List[int]):
    happiness = 0
    for i in range(0, len(path_)):
        happiness += data_[path_[0]][path_[-1]] if (i==0) else data_[path_[i]][path_[i-1]]
        happiness += data_[path_[i]][path_[0]] if (i == (len(path_) - 1)) else data_[path_[i]][path_[i+1]]
    return happiness

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
        lines = readLines(self.filename)

        peoples = set()
        data = dict()
        
        for line in lines:
            found = re.fullmatch("(.+) would (.+) (.+) happiness units by sitting next to (.+).", line)
            peoples.add(found.group(1))
            peoples.add(found.group(4))
            
            data.setdefault(found.group(1), dict())[found.group(4)] = int(found.group(3)) if (found.group(2) == "gain") else -int(found.group(3))
            
        # Part 1
        for path in permutations(peoples):
            h = computeHappiness(data, path)
            self.result1 = max(self.result1, h)
            
        # Part 2
        for people in peoples:
            data.setdefault("me", dict())[people] = 0
            data.setdefault(people, dict())["me"] = 0         
        peoples.add("me")
        
        for path in permutations(peoples):
            h = computeHappiness(data, path)
            self.result2 = max(self.result2, h)
        
############################################################
# MAIN
############################################################
filename = "data/" + INPUT_FILES[TEST]
p = Puzzle(filename)
p.run()
print("Result 1: " + str(p.getResult1()))
print("Result 2: " + str(p.getResult2()))           
