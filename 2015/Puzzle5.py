############################################################
# Import
############################################################
from Utils import *
import re

############################################################
# Class Puzzle5
############################################################
class Puzzle5:
    def __init__(self, filename_):
        self.filename = filename_
        self.result1 = 0
        self.result2 = 0
    
    def getResult1(self):
        return self.result1

    def getResult2(self):
        return self.result2
    
    def checkPart2Cond1(self, word) -> bool:
        for i in range(len(word) - 3):
            for j in range(i+2, len(word) - 1):
                if ((word[i] == word[j]) and (word[i+1] == word[j+1])):
                    return True
        return False
    
    def checkkPart2Cond2(self, word) -> bool:
        for i in range(len(word) - 2):
            if (word[i] == word[i+2]):
                return True
        return False
        

    def run(self):
        words = readLines(self.filename)
        
        for word in words:
            b1 = (re.subn("[aeiou]", '', word)[1] > 2)
            b2 = not (re.search("([a-z])\\1", word) == None)
            b3 = re.search("(?:ab|cd|pq|xy)", word) == None
            
            if (b1 and b2 and b3):
                self.result1 += 1
                
            if (self.checkPart2Cond1(word) and self.checkkPart2Cond2(word)):
                self.result2 += 1
    
        return            
