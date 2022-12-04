############################################################
# Import
############################################################
from Utils import *
from itertools import groupby

############################################################
# Static Methods
############################################################
def compute(text_: str) -> str:
    result = ""
    for i,j in groupby(text_):
        result += str(len(list(j))) + str(i)
    
    return result

############################################################
# Class Puzzle10
############################################################
class Puzzle10:
    def __init__(self, filename_: str):
        self.filename = filename_
        self.result1 = 0
        self.result2 = 0
    
    def getResult1(self) -> int:
        return self.result1

    def getResult2(self) -> int:
        return self.result2

    def run(self):
        text = readFile(self.filename)
        
        # Part 1
        data = text
        for _ in range(40):
            data = compute(data)
    
        self.result1 = len(data)
        
        # Part 2
        data = text
        for _ in range(50):
            data = compute(data)
    
        self.result2 = len(data)
            
        return            
