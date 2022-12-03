############################################################
# Import
############################################################
from Utils import *

############################################################
# Class Puzzle3
############################################################
class Puzzle3:
    def __init__(self, filename_):
        self.filename = filename_
        self.result1 = 0
        self.result2 = 0
    
    def getResult1(self):
        return self.result1

    def getResult2(self):
        return self.result2

    def run(self):
        lines = readLines(self.filename)
   
        # Part 1
        for line in lines:
            item1 = line[:(int)(len(line)/2)]
            item2 = line[(int)(len(line)/2):]
            matches = set(item1).intersection(item2)
        
            for m in matches:
                p = (ord(m) - 64 + 26) if m.isupper() else (ord(m) - 96)
                self.result1 += p
                
        # Part 2
        for i in range(0, len(lines) - 2, 3):
            matches = set(lines[i]).intersection(lines[i+1]).intersection(lines[i+2])
            
            for m in matches:
                p = (ord(m) - 64 + 26) if m.isupper() else (ord(m) - 96)
                self.result2 += p
    
        return            
