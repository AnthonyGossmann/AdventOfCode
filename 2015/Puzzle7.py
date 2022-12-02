############################################################
# Import
############################################################
from Utils import *

############################################################
# Class Wire
############################################################
class Wire:
    def __init__(self, name_):
        self.name = name_
        self.action = 0
        self.parameter = 0
        self.updated = False
        self.value = 0
        
    def getName(self):
        return self.name
    
    def isUpdated(self):
        return self.updated
    
    def getValue(self):
        return self.value
    
    def setValue(self, value_):
        self.value = value_
        self.updated = True
        
    def getWire(self, wires_, name_) -> Wire:
        for wire in wires_:
            if (wire.getName() == name_):
                return 
############################################################
# Class Puzzle7
############################################################
class Puzzle7:
    def __init__(self, filename_):
        self.filename = filename_
        self.result1 = 0
        self.result2 = 0
    
    def getResult1(self):
        return self.result1

    def getResult2(self):
        return self.result2

    def run(self):
    
        return            
