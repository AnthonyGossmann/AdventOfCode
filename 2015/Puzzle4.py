############################################################
# Import
############################################################
from Utils import *
import hashlib

############################################################
# Class Puzzle4
############################################################
class Puzzle4:
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
    
        return            
