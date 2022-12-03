############################################################
# Import
############################################################
from Utils import *
from typing import List
import string
import numpy as np
import itertools as it
import math

############################################################
# Static Methods
############################################################
def perm(k: int):
    f_k = math.factorial(k)
    A = np.empty((f_k, k))
    for i,perm in enumerate(it.permutations(range(k))):
        A[i,:] = perm
    return A

def searchData(data_, from_, to_):
    for i in range(0, len(data_) - 2, 3):
        print(i)
        if ((data_[i] == from_) and (data_[i+1] == to_)):
            return data_[i+2]
    return -1

############################################################
# Class Puzzle9
############################################################
class Puzzle9:
    def __init__(self, filename_: str):
        self.filename = filename_
        self.result1 = 0
        self.result2 = 0
    
    def getResult1(self) -> int:
        return self.result1

    def getResult2(self) -> int:
        return self.result2

    def run(self):
        data = readSplit(self.filename, "to|[ =\n]")
        
        cities = []
        for i in range(len(data)):
            if not re.search("^[0-9]+$", data[i]):
                if data[i] not in cities:
                    cities.append(data[i])
                idx = cities.index(data[i])
                data[i] = data[i].replace(data[i], str(idx))
            data[i] = int(data[i])
        
        P = perm(len(cities))

        dist = []
        for i in range(0, len(P)):
            for j in range(0, len(P[0]) - 1):
                f = int(P[i][j])
                t = int(P[i][j+1])
                dist += searchData(data, f, t)
                
        self.result1 = min(dist)
    
        return            
