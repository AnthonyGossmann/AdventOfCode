############################################################
# Import
############################################################
from Utils import *
import re

############################################################
# Class Puzzle2
############################################################
class Puzzle2:
    def __init__(self, filename_):
        self.filename = filename_
        self.result1 = 0
        self.result2 = 0
    
    def getResult1(self):
        return self.result1

    def getResult2(self):
        return self.result2
    
    def getScore1(self, p1, p2):
        if ((p2 == 3) and (p1 == 1)):
            return p2
        elif (((p2 == 1) and (p1 == 3)) or (p2 > p1)):
            return p2 + 6
        elif (p2 == p1):
            return p2 + 3
        return p2
    
    def getScore2(self, p1, outcome):
        if (outcome == 1):
            return (3 if (p1 == 1) else (p1 - 1))
        elif (outcome == 2):
            return p1 + 3
        else:
            return (1 if (p1 == 3) else (p1 + 1)) + 6

    def run(self):
        text = readFile(self.filename)
        text = re.sub("[AX]", "1", text)
        text = re.sub("[BY]", "2", text)
        text = re.sub("[CZ]", "3", text)    
        data = apply(int, re.split("[ \n]", text))

        for i in range(0, len(data) - 1, 2):
            self.result1 += self.getScore1(data[i], data[i+1])
            self.result2 += self.getScore2(data[i], data[i+1]) 
    
        return            
