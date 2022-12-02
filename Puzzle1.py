############################################################
# Import
############################################################
from Utils import *

############################################################
# Class Puzzle1
############################################################
class Puzzle1:
    def __init__(self, filename_):
        self.filename = filename_
        self.result1: int = 0
        self.result2 = 0
    
    def getResult1(self):
        return self.result1

    def getResult2(self):
        return self.result2

    def run(self):
        lines = readLines(self.filename)
        data = []
        
        current = 0
        for line in lines:
            if (len(line) == 0):
                data.append(current)
                current = 0
            else:
                current += int(line)
        data = sorted(data)
        
        self.result1 = data[-1]
        self.result2 = sum(data[-3:])        
    
        return            
