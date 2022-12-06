############################################################
# Import
############################################################
from Utils import *
from itertools import permutations

############################################################
# Static Methods
############################################################
def computeHappiness(data_, path_):
    happiness = 0
    for i in range(0, len(path_)):
        happiness += data_[path_[0] + "_" + path_[len(path_) - 1]] if (i==0) else data_[path_[i] + "_" + path_[i-1]]
        happiness += data_[path_[i] + "_" + path_[0]] if (i == (len(path_) - 1)) else data_[path_[i] + "_" + path_[i+1]]
    return happiness

############################################################
# Class Puzzle13
############################################################
class Puzzle13:
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
        
        peoples = []
        data = {}
        for line in lines:
            found = re.fullmatch("(.+) would (.+) (.+) happiness units by sitting next to (.+).", line)
    
            if (found.group(1) not in peoples):
                peoples.append(found.group(1))
            if (found.group(4) not in peoples):
                peoples.append(found.group(4))
        
            data[found.group(1) + "_" + found.group(4)] = int(found.group(3)) if (found.group(2) == "gain") else -int(found.group(3))

        # Part 1
        for path in permutations(peoples):
            h = computeHappiness(data, path)
            if (h > self.result1):
                self.result1 = h
    
        # Part 2
        for people in peoples:
            data["me_" + people] = 0
            data[people + "_me"] = 0
        peoples.append("me")
        
        for path in permutations(peoples):
            h = computeHappiness(data, path)
            if (h > self.result2):
                self.result2 = h
        
        return            
