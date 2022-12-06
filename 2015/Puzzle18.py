############################################################
# Import
############################################################
from Utils import *
from typing import List
from itertools import product

############################################################
# Class Light
############################################################
class Light:
    def __init__(self, x_: int, y_: int, state_: bool):
        self.key = str(x_) + "," + str(y_)
        self.x = x_
        self.y = y_
        self.state = state_
        self.neighbour = self.getNeighbours()
        
    def getNeighbours(self) -> List:
        ngh = []
        x = [self.x - 1, self.x, self.x + 1]
        y = [self.y - 1, self.y, self.y + 1]
        
        x = [x[i] for i in range(len(x)) if ((x[i] != -1) and (x[i] != 100))]
        y = [y[i] for i in range(len(y)) if ((y[i] != -1) and (y[i] != 100))]

        for i,j in product(x,y):
            if ((i != self.x) or (j != self.y)):
                ngh.append(str(i) + "," + str(j))
        
        return ngh
    
    def getLight(self, lights_, key_):
        if (key_ in lights_.keys()):
            return lights_[key_]
        raise Exception("Point not found (" + key_ + ")")
    
    def updateState(self, lights_):
        ctr = 0
        for ngh in self.neighbour:
            if (self.getLight(lights_, ngh).state):
                ctr += 1
        
        if (self.state and (ctr != 2) and (ctr != 3)):
            self.state = False
        elif (not self.state and (ctr == 3)):
            self.state = True
            
        return self
                
############################################################
# Class Puzzle18
############################################################
class Puzzle18:
    def __init__(self, filename_: str):
        self.filename = filename_
        self.result1 = 0
        self.result2 = 0
        self.lights = {}
    
    def getResult1(self) -> int:
        return self.result1

    def getResult2(self) -> int:
        return self.result2
    
    def run(self):
        lines = readLines(self.filename)
        
        for i in range(len(lines)):
            for j in range(len(lines[i])):
                key = str(i) + "," + str(j)
                if (lines[i][j] == '#'):
                    self.lights[key] = Light(i, j, True)
                else:
                    self.lights[key] = Light(i, j, False)

        # Part 1
        ltEnd = self.lights.copy()
        for i in range(100):
            print(i)
            ltStart = ltEnd.copy()
            ltEnd.clear()
            
            for light in ltStart.values():
                ltEnd[light.key] = light.updateState(ltStart)
        
        for light in ltEnd.values():
            if light.state:
                self.result1 += 1
    
        return            
