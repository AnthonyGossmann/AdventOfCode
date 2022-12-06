############################################################
# Import
############################################################
from Utils import *

############################################################
# Static Methods
############################################################
def findMarker(text: str, length: int) -> int:
    for i in range(len(text) - length + 1):
        sub = list(set(text[i:i+length]))
        if (len(sub) == length):
            return i + length

    return -1

############################################################
# Class Puzzle6
############################################################
class Puzzle6:
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

        self.result1 = findMarker(text, 4)
        self.result2 = findMarker(text, 14)
   
        return            
