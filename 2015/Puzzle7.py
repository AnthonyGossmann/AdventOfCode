############################################################
# Import
############################################################
from Utils import *
from typing import List
import re

############################################################
# Static Methods
############################################################
def getAction(tokens_: [str]) -> str:
    if (("1" in tokens_) and ("AND" in tokens_)):
        return "1AND"
    elif ("AND" in tokens_):
        return "AND"
    elif ("OR" in tokens_):
        return "OR"
    elif ("LSHIFT" in tokens_):
        return "LSHIFT"
    elif ("RSHIFT" in tokens_):
        return "RSHIFT"
    elif ("NOT" in tokens_):
        return "NOT"
    return "ASSIGN"

def getWire(wires_: List, name_: str) -> int:
    for i in range(len(wires_)):
        if (wires_[i].getName() == name_):
            return i
    return -1

def update(wires_: List):
    completed = False
    while not completed:
        completed = True
        for wire in wires_:
            wire.update(wires_)
            completed &= wire.isUpdated()

############################################################
# Class Wire
############################################################
class Wire:
    def __init__(self, name_: str):
        self.name = name_
        self.action = ""
        self.parameter = 0
        self.updated = False
        self.value = 0
        self.inputs = []
        
    def getName(self) -> str:
        return self.name
    
    def isUpdated(self) -> bool:
        return self.updated
    
    def getValue(self) -> int:
        return self.value
    
    def setValue(self, value_: int):
        self.value = value_
        self.updated = True
        
    def reset(self):
        if (len(self.inputs) != 0):
            self.value = 0
            self.updated = False
    
    def connect(self, tokens_: List[str], wires_: List):
        self.action = getAction(tokens_)
        
        if (self.action == "1AND"):
            self.parameter = 1
            self.inputs.append(getWire(wires_, tokens_[2]))
        elif (self.action == "AND"):
            self.inputs.append(getWire(wires_, tokens_[0]))
            self.inputs.append(getWire(wires_, tokens_[2]))
        elif (self.action == "OR"):
            self.inputs.append(getWire(wires_, tokens_[0]))
            self.inputs.append(getWire(wires_, tokens_[2]))
        elif (self.action == "LSHIFT"):
            self.inputs.append(getWire(wires_, tokens_[0]))
            self.parameter = int(tokens_[2])
        elif (self.action == "RSHIFT"):
            self.inputs.append(getWire(wires_, tokens_[0]))
            self.parameter = int(tokens_[2])
        elif (self.action == "NOT"):
            self.inputs.append(getWire(wires_, tokens_[1]))
        else:
            try:
                self.value = int(tokens_[0])
                self.updated = True
            except:
                self.inputs.append(getWire(wires_, tokens_[0]))
        
    
    def update(self, wires_):
        if self.updated:
            return
        
        inputsUpdated = True
        for i in self.inputs:
            inputsUpdated &= wires_[i].isUpdated()
        if not inputsUpdated:
            return
        
        if (self.action == "1AND"):
            self.value = self.parameter & wires_[self.inputs[0]].getValue()
        elif (self.action == "AND"):
            self.value = wires_[self.inputs[0]].getValue() & wires_[self.inputs[1]].getValue()
        elif (self.action == "OR"):
            self.value = wires_[self.inputs[0]].getValue() | wires_[self.inputs[1]].getValue()
        elif (self.action == "LSHIFT"):
            self.value = wires_[self.inputs[0]].getValue() << self.parameter
        elif (self.action == "RSHIFT"):
            self.value = wires_[self.inputs[0]].getValue() >> self.parameter
        elif (self.action == "NOT"):
            self.value = ~wires_[self.inputs[0]].getValue() & 0xFFFF
        else:
            self.value = wires_[self.inputs[0]].getValue()
        
        self.updated = True
        
        return
            
############################################################
# Class Puzzle7
############################################################
class Puzzle7:
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
        
        # Create all wires
        wires = []
        for line in lines:
            wires.append(Wire(re.split(" ", line)[-1]))       
            
        # Connect
        for line in lines:
            tokens = list(filter(None, re.split(" ", line)))
            idx = getWire(wires, tokens[-1])
            wires[idx].connect(tokens, wires)
        
        # Part 1
        update(wires)     
        self.result1 = wires[getWire(wires, "a")].getValue()
        
        # Part 2
        wires[getWire(wires, "b")].setValue(self.result1)
        for wire in wires:
            wire.reset()
            
        update(wires)     
        self.result2 = wires[getWire(wires, "a")].getValue()
        
        return            
