############################################################
# Import
############################################################
from Utils import *
import re
import numpy as np

############################################################
# Class Puzzle2
############################################################
class Puzzle2:
    def __init__(self, filename_):
        self.filename = filename_
        self.result1 = 0
        self.result2 = 0
    
    def getResult1(self):
        return self.result1

    def getResult2(self):
        return self.result2

    def run(self):
        data = np.array(apply(int, readSplit(self.filename, "[x\n]")))
        data = np.reshape(data, ((int)(len(data) / 3), 3))
        data.sort()

        for i in range(len(data)):
            self.result1 += 3 * data[i, 0] * data[i, 1] + 2 * data[i, 1] * data[i, 2] + 2 * data[i, 0] * data[i, 2]
            self.result2 += 2 * (data[i, 0] + data[i, 1]) + data[i, 0] * data[i, 1] * data[i, 2]

        return            
