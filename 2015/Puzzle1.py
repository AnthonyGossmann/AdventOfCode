############################################################
# Import
############################################################
from Utils import *

############################################################
# Class Puzzle1
############################################################
class Puzzle1:
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
        text = readFile(self.filename)
        
        self.result1 = text.count('(') - text.count(')')
        
        self.result2 = 1
        while ((text[:self.result2].count('(') - text[:self.result2].count(')')) != -1):
            self.result2 += 1
    
    
        return            
