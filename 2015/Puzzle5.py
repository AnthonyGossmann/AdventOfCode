############################################################
# Import
############################################################
from Utils import *
import re

############################################################
# Static Methods
############################################################
def checkP2Cnd1(word: str) -> bool:
    for i in range(len(word) - 3):
        for j in range(i+2, len(word) - 1):
            if ((word[i] == word[j]) and (word[i+1] == word[j+1])):
                return True
    return False

def checkP2Cnd2(word: str) -> bool:
    for i in range(len(word) - 2):
        if (word[i] == word[i+2]):
            return True
    return False

############################################################
# Class Puzzle5
############################################################
class Puzzle5:
    def __init__(self, filename_: str):
        self.filename = filename_
        self.result1 = 0
        self.result2 = 0
    
    def getResult1(self) -> int:
        return self.result1

    def getResult2(self) -> int:
        return self.result2
    
    
        

    def run(self):
        words = readLines(self.filename)
        
        for word in words:
            b1 = (re.subn("[aeiou]", '', word)[1] > 2)
            b2 = not (re.search("([a-z])\\1", word) == None)
            b3 = re.search("(?:ab|cd|pq|xy)", word) == None
            
            self.result1 += int(b1 and b2 and b3)
            self.result2 += int(checkP2Cnd1(word) and checkP2Cnd2(word))
    
        return            
