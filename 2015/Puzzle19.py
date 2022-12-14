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
INPUT_FILES = ["19.txt", "19.ex"]

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
        
        cmds = []
        molecule = ""
        for line in lines:
            if(len(line) == 0):
                continue
            if ("=>" in line):
                found = re.fullmatch("(.+) => (.+)", line)
                cmds.append([found.group(1), found.group(2)])
            else:
                molecule = line
                
        # Part 1
        molecules = []
        for cmd in cmds:
            indexes_object = re.finditer(cmd[0], molecule)
            indexes = [index.start() for index in indexes_object]
            for index in indexes:
                s = molecule[:index] + cmd[1] + molecule[index + len(cmd[0]):]
                if s not in molecules:
                    molecules.append(s)

        self.result1 = len(molecules)
        
        # Part 2
        target = molecule 
        while (target != "e"):
            for cmd in cmds:
                self.result2 += target.count(cmd[1])
                target = target.replace(cmd[1], cmd[0])
                
############################################################
# MAIN
############################################################
filename = "data/" + INPUT_FILES[TEST]
p = Puzzle(filename)
p.run()
print("Result 1: " + str(p.getResult1()))
print("Result 2: " + str(p.getResult2()))            
