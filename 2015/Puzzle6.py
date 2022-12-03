############################################################
# Import
############################################################
from Utils import *
import numpy as np

############################################################
# Class Puzzle6
############################################################
class Puzzle6:
    def __init__(self, filename_: str):
        self.filename = filename_
        self.result1 = 0
        self.result2 = 0
        self.lights = np.zeros((1000, 1000))
    
    def getResult1(self) -> int:
        return self.result1

    def getResult2(self) -> int:
        return self.result2
    

    def run(self):
        text = readFile(self.filename)
        text = text.replace("turn off", "0").replace("turn on", "1").replace("toggle", "3").replace("through", "")
        lines = list(filter(None, re.split("[\n]", text)))
        
        # Part 1
        for line in lines:
            data = apply(int, filter(None, re.split("[ ,]", line)))
            
            for i in range(data[1], data[3]+1):
                for j in range(data[2], data[4]+1):
                    if (data[0] == 0):
                        self.lights[i][j] = 0
                    elif (data[0] == 1):
                        self.lights[i][j] = 1
                    else:
                        self.lights[i][j] = not self.lights[i][j]
                
        self.result1 = (int)(self.lights.sum())
        
        # Part 2
        self.lights = np.zeros((1000, 1000))
        for line in lines:
            data = apply(int, filter(None, re.split("[ ,]", line)))
            
            for i in range(data[1], data[3]+1):
                for j in range(data[2], data[4]+1):
                    if (data[0] == 0):
                        self.lights[i][j] = 0 if (self.lights[i][j] == 0) else (self.lights[i][j] - 1)
                    elif (data[0] == 1):
                        self.lights[i][j] += 1
                    else:
                        self.lights[i][j] += 2

        self.result2 = (int)(self.lights.sum())
    
        return            
