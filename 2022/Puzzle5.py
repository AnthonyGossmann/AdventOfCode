############################################################
# Import
############################################################
from Utils import *
import re

############################################################
# Class Puzzle5
############################################################
class Puzzle5:
    def __init__(self, filename_: str):
        self.filename = filename_
        self.result1 = ""
        self.result2 = ""
    
    def getResult1(self) -> str:
        return self.result1

    def getResult2(self) -> str:
        return self.result2
    
    def loadCrates(self):
        text = readFile(self.filename)
        lines = text.split("\n")
        
        crates = {}
        instr = []
        for line in lines:
            if ('[' in line):
                # Load Crates
                tokens = re.split("[\s]{4}", line)
                data = []
                for token in tokens:
                    data += re.split(" ", token)

                data = [x.replace('[', '').replace(']', '') for x in data]
                
                for i in range(len(data)):
                    if (i+1) not in crates.keys():
                        crates[i+1] = []
                    if not (data[i] == ''):
                        crates[i+1].insert(0, data[i])
                        
            elif ("move" in line):
                 found =  re.fullmatch("move (.+) from (.+) to (.+)", line)
                 instr.append([int(found.group(1)), int(found.group(2)), int(found.group(3))])
        
        return [crates, instr]
    
    def applyInstr(self, crates_, instr_, mult = False):
        if mult:
                items = crates_[instr_[1]][-instr_[0]:]
                crates_[instr_[1]] = crates_[instr_[1]][:-instr_[0]]
                crates_[instr_[2]] += items
        else:
            for i in range(instr_[0]):
                item = crates_[instr_[1]][-1]
                crates_[instr_[1]] = crates_[instr_[1]][:-1]
                crates_[instr_[2]].append(item)
            
        return crates_

    def run(self):
        text = readFile(self.filename)
        lines = text.split("\n")
        
        # Part 1
        [crates, instr] = self.loadCrates()
        for ins in instr:
            crates = self.applyInstr(crates, ins)
        
        for key in crates.keys():
            if not (len(crates[key]) == 0):
                self.result1 += crates[key][-1]
        
        # Part 2
        [crates, instr] = self.loadCrates()
        for ins in instr:
            crates = self.applyInstr(crates, ins, True)
            
        for key in crates.keys():
            if not (len(crates[key]) == 0):
                self.result2 += crates[key][-1]
        
        return            
