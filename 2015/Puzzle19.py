############################################################
# Import
############################################################
from Utils import *

############################################################
# Class Puzzle19
############################################################
class Puzzle19:
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
        
        instructions = []
        molecule = ""
        for line in lines:
            if(len(line) == 0):
                continue
            if ("=>" in line):
                found = re.fullmatch("(.+) => (.+)", line)
                instructions.append([found.group(1), found.group(2)])
            else:
                molecule = line
                
        # Part 1
        molecules = []
        for ins in instructions:
            indexes_object = re.finditer(ins[0], molecule)
            indexes = [index.start() for index in indexes_object]
            for index in indexes:
                s = molecule[:index] + ins[1] + molecule[index + len(ins[0]):]
                if s not in molecules:
                    molecules.append(s)

        self.result1 = len(molecules)
        
        # Part 2
        target = molecule 
        while (target != "e"):
            for ins in instructions:
                self.result2 += target.count(ins[1])
                target = target.replace(ins[1], ins[0])
                
        return            
