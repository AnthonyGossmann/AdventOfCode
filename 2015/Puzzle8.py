############################################################
# IMPORT
############################################################
from Utils import *
import string

############################################################
# CONFIGURATION
############################################################
TEST = 0

############################################################
# DEFINITIONS
############################################################
INPUT_FILES = ["08.txt", "08.ex"]

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
        lines = readLines(self.filename)
        
        rgxHex = re.compile(r"\\x[0-9a-f]{2}") # \0x..
        rgxEsc = re.compile(r"\\[\"\\]") # \\ and \#
        rgxEscHex = re.compile(r"\\\\x[0-9a-f]{2}") # \\0x..
        rgxEscHex2 = re.compile(r"\\\\\\x[0-9a-f]{2}") # \\\0x..
        
        for line in lines:
            line = line.strip() 
            
            lHex = rgxHex.findall(line)
            lEsc = rgxEsc.findall(line)
            lEscHex = rgxEscHex.findall(line)
            lEscHex2 = rgxEscHex2.findall(line)

            codeLen = len(line)
            memLen = codeLen - 2 - len(lEsc) - 3 * (len(lHex) - len(lEscHex) + len(lEscHex2))
            memLen2 = codeLen + 4 + 2 * len(lEsc) + len(lHex) - len(lEscHex) + len(lEscHex2)

            self.result1 += (codeLen - memLen)
            self.result2 += (memLen2 - codeLen)
        
############################################################
# MAIN
############################################################
filename = "data/" + INPUT_FILES[TEST]
p = Puzzle(filename)
p.run()
print("Result 1: " + str(p.getResult1()))
print("Result 2: " + str(p.getResult2()))            
