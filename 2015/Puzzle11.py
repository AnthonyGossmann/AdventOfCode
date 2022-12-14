############################################################
# IMPORT
############################################################
from Utils import *

############################################################
# CONFIGURATION
############################################################
TEST = 0

############################################################
# DEFINITIONS
############################################################
INPUT_FILES = ["11.txt", "11.ex"]

############################################################
# METHODS
############################################################
def checkPwd(pwd_: str) -> bool:
    b1 = False
    for i in range(len(pwd_) - 2):
        if (ord(pwd_[i]) == (ord(pwd_[i+1]) - 1) == (ord(pwd_[i+2]) -2)):
            b1 = True
            break
        
    b2 = True
    if (('i' in pwd_) or ('o' in pwd_) or ('l' in pwd_)):
        b2 = False
        
    ctr3 = 0
    i = 0
    while (i<(len(pwd_) - 1)):
        if (pwd_[i] == pwd_[i+1]):
            ctr3 += 1
            i += 2
        else:
            i += 1
    b3 = (ctr3 >= 2)
    
    return (b1 and b2 and b3)

def nextPwd(pwd_: str) -> str:
    rev = pwd_[::-1]
    
    i = 0
    while (i<len(rev)):
        if (rev[i] == 'z'):
            rev = rev[:i] + 'a' + rev[i+1:]
            i += 1
        else:
            c = chr(ord(rev[i]) + 1)
            rev = rev[:i] + c + rev[i+1:]
            break
    
    result = rev[::-1]
    
    return result

############################################################
# CLASS PUZZLE
############################################################
class Puzzle:
    filename: str
    result1: str
    result2: str
    
    def __init__(self, filename_: str):
        self.filename = filename_
        self.result1 = ""
        self.result2 = ""
    
    def getResult1(self) -> str:
        return self.result1

    def getResult2(self) -> str:
        return self.result2

    def run(self):
        text = readFile(self.filename)
       
        # Part 1
        result = text
        while True:
            result = nextPwd(result)
            if checkPwd(result):
                break
            
        self.result1 = result
        
        # Part 2
        while True:
            result = nextPwd(result)
            if checkPwd(result):
                break
            
        self.result2 = result

############################################################
# MAIN
############################################################
filename = "data/" + INPUT_FILES[TEST]
p = Puzzle(filename)
p.run()
print("Result 1: " + str(p.getResult1()))
print("Result 2: " + str(p.getResult2()))        
