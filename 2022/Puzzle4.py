############################################################
# Import
############################################################
from Utils import *

############################################################
# Class Puzzle4
############################################################
class Puzzle4:
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
        
        for line in lines:
            found = re.fullmatch("(.+)-(.+),(.+)-(.+)", line)
            items1 = [i for i in range(int(found.group(1)), int(found.group(2))+1)]
            items2 = [i for i in range(int(found.group(3)), int(found.group(4))+1)]

            self.result1 += all(item in items1 for item in items2) + all(item in items2 for item in items1) - (items1 == items2)
            self.result2 += any(item in items1 for item in items2)
    
        return            
