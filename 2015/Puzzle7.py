############################################################
# Import
############################################################
from Utils import *
import typing
from typing import List
from typing import NewType
from typing import Dict
from enum import Enum
from dataclasses import dataclass
import re

############################################################
# Definitions
############################################################
class Action(Enum):
    ASSIGN = 0,
    AND1 = 1,
    AND = 2,
    OR = 3,
    LSHIFT = 4,
    RSHIFT = 5,
    NOT = 6
    
Action = Enum("Action", ["ASSIGN", "AND1", "AND", "OR", "LSHIFT", "RSHIFT", "NOT"])

############################################################
# Static Methods
############################################################
def getAction(tokens_: List[str]) -> Action:
    if (("1" in tokens_) and ("AND" in tokens_)):
        return Action.AND1
    elif ("AND" in tokens_):
        return Action.AND
    elif ("OR" in tokens_):
        return Action.OR
    elif ("LSHIFT" in tokens_):
        return Action.LSHIFT
    elif ("RSHIFT" in tokens_):
        return Action.RSHIFT
    elif ("NOT" in tokens_):
        return Action.NOT
    return Action.ASSIGN

############################################################
# Class Wire
############################################################
Wire = typing.NewType("Wire", None)
@dataclass()
class Wire:
    name: str
    action: Action
    parameter: int
    updated: bool
    value: int
    inputs: List[Wire]
    
    def __init__(self, name_: str):
        self.name = name_
        self.parameter = 0
        self.updated = False
        self.value = 0
        self.inputs = []
        
    def reset(self):
        if (len(self.inputs) != 0):
            self.value = 0
            self.updated = False
        
    def setAction(self, wires_: Dict[str, Wire], tokens_: List[str]):
        self.action = getAction(tokens_)
        
        if (self.action == Action.AND1):
            self.parameter = 1
            self.inputs.append(wires_[tokens_[2]])
        elif (self.action == Action.AND):
            self.inputs.append(wires_[tokens_[0]])
            self.inputs.append(wires_[tokens_[2]])
        elif (self.action == Action.OR):
            self.inputs.append(wires_[tokens_[0]])
            self.inputs.append(wires_[tokens_[2]])
        elif (self.action == Action.LSHIFT):
            self.inputs.append(wires_[tokens_[0]])
            self.parameter = int(tokens_[2])
        elif (self.action == Action.RSHIFT):
            self.inputs.append(wires_[tokens_[0]])
            self.parameter = int(tokens_[2])
        elif (self.action == Action.NOT):
            self.inputs.append(wires_[tokens_[1]])
        else:
            try:
                self.value = int(tokens_[0])
                self.updated = True
            except:
                self.inputs.append(wires_[tokens_[0]])
                
    def update(self):
        if self.updated:
            return
        
        for wire in self.inputs:
            if not wire.updated:
                wire.update()
        
        if (self.action == Action.AND1):
            self.value = self.parameter & self.inputs[0].value
        elif (self.action == Action.AND):
            self.value = self.inputs[0].value & self.inputs[1].value
        elif (self.action == Action.OR):
            self.value = self.inputs[0].value | self.inputs[1].value
        elif (self.action == Action.LSHIFT):
            self.value = (self.inputs[0].value << self.parameter) & 0xFFFF
        elif (self.action == Action.RSHIFT):
            self.value = (self.inputs[0].value >> self.parameter) & 0xFFFF
        elif (self.action == Action.NOT):
            self.value = ~self.inputs[0].value & 0xFFFF
        else:
            self.value = self.inputs[0].value
            
        self.updated = True
            
############################################################
# Class Puzzle7
############################################################
class Puzzle7:
    filename: str
    result1: int
    result2: int
    wires: Dict[str,Wire]
    
    def __init__(self, filename_: str):
        self.filename = filename_
        self.result1 = 0
        self.result2 = 0
        self.wires = {}
    
    def getResult1(self) -> int:
        return self.result1

    def getResult2(self) -> int:
        return self.result2
    
    def reset(self):
        for wire in self.wires.values():
            wire.reset()
    
    def run(self):
        lines = readLines(self.filename)
        
        # Create all wires
        for line in lines:
            wire = re.split(" ", line)[-1]
            if wire not in self.wires.keys():
                self.wires[wire] = Wire(wire)

        # Set actions and links
        for line in lines:
            tokens = list(filter(None, re.split(" ", line)))
            self.wires[tokens[-1]].setAction(self.wires, tokens)
            
        # Part 1
        self.wires["a"].update()
        self.result1 = self.wires["a"].value
        
        # Part 2
        self.reset()
        self.wires["b"].value = self.result1
        self.wires["a"].update()
        self.result2 = self.wires["a"].value
        
        return            
