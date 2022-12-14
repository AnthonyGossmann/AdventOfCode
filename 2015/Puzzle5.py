############################################################
# IMPORT
############################################################
from Utils import *
import re

############################################################
# CONFIGURATION
############################################################
TEST = 0

############################################################
# DEFINITIONS
############################################################
INPUT_FILES = ["05.txt", "05.ex"]

############################################################
# METHODS
############################################################
def checkP2Cnd1(word_: str) -> bool:
    for i in range(len(word_) - 3):
        for j in range(i+2, len(word_) - 1):
            if ((word_[i] == word_[j]) and (word_[i+1] == word_[j+1])):
                return True
    return False

def checkP2Cnd2(word_: str) -> bool:
    for i in range(len(word_) - 2):
        if (word_[i] == word_[i+2]):
            return True
    return False

############################################################
# CLASS PUZZLE
############################################################
class Puzzle:
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
        words = readLines(self.filename)
        
        for word in words:
            b1 = (re.subn("[aeiou]", '', word)[1] > 2)
            b2 = (re.search("([a-z])\\1", word) != None)
            b3 = re.search("(?:ab|cd|pq|xy)", word) == None
            
            self.result1 += int(b1 and b2 and b3)
            self.result2 += int(checkP2Cnd1(word) and checkP2Cnd2(word))
    
############################################################
# MAIN
############################################################
filename = "data/" + INPUT_FILES[TEST]
p = Puzzle(filename)
p.run()
print("Result 1: " + str(p.getResult1()))
print("Result 2: " + str(p.getResult2()))              
