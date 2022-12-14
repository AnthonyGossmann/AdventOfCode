############################################################
# IMPORT
############################################################
from Utils import *
import hashlib

############################################################
# CONFIGURATION
############################################################
TEST = 0

############################################################
# DEFINITIONS
############################################################
INPUT_FILES = ["04.txt", "04.ex"]

############################################################
# METHODS
############################################################

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
        key = readFile(self.filename)

        result = 1
        found5 = False
        found6 = False
        
        while not found5 or not found6:
            m = hashlib.md5()
            s = key + str(result)
            m.update(s.encode('utf-8'))
            digest = m.hexdigest()
            
            if not found5 and digest.startswith("00000"):
                self.result1 = result
                found5 = True
            if not found6 and digest.startswith("000000"):
                self.result2 = result
                found6 = True
            result += 1
    
############################################################
# MAIN
############################################################
filename = "data/" + INPUT_FILES[TEST]
p = Puzzle(filename)
p.run()
print("Result 1: " + str(p.getResult1()))
print("Result 2: " + str(p.getResult2()))             
