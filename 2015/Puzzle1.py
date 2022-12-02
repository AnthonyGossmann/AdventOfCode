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
        text = readFile(self.filename)
        self.result1 = text.count('(') - text.count(')')
        
        self.result2 = 1
        while ((text[:self.result2].count('(') - text[:self.result2].count(')')) != -1):
            self.result2 += 1
    
    
        return            
