############################################################
# IMPORT
############################################################
from Utils import *
from itertools import product
import typing
from typing import List
from typing import Tuple
from typing import NewType
from dataclasses import dataclass
import re
import numpy as np

############################################################
# CONFIGURATION
############################################################
TEST = 0

############################################################
# DEFINITIONS
############################################################
INPUT_FILES = ["15.txt", "15.ex"]

############################################################
# METHODS
############################################################
def distance(p1_: Tuple[int,int], p2_: Tuple[int,int]) -> int:
    return abs(p2_[0] - p1_[0]) + abs(p2_[1] - p1_[1])

def getEmptyX(ranges_: List, limit_: int) -> List:
    i = 0
    right = ranges_[i][1]
    
    while (i < len(ranges_)):
        if (ranges_[i][0] <= right):
            right = max(right, ranges_[i][1]) 
        i += 1

    i = len(ranges_) - 1
    left = ranges_[i][0]
    
    while (i >= 0):
        if (ranges_[i][1] >= left):
            left = min(left, ranges_[i][0])
        i -= 1
    
    left = max(0, left)
    right = min(limit_, right)
    
    if (left > right):
        return right

    return -1
    
    
############################################################
# CLASS PUZZLE
############################################################
class Puzzle:
    filename: str
    result1: int
    result2: int
    sensors: List
    beacons: List
    
    def __init__(self, filename_: str):
        self.filename = filename_
        self.result1 = 0
        self.result2 = 0
        self.sensors = []
        self.beacons = []
    
    def getResult1(self) -> int:
        return self.result1

    def getResult2(self) -> int:
        return self.result2
    
    def load(self):
        lines = readLines(self.filename)
        edges = [1E9,0,1E9,0]
        for line in lines:
            found = re.fullmatch("Sensor at x=(.+), y=(.+): closest beacon is at x=(.+), y=(.+)", line)
            self.sensors.append((int(found.group(1)), int(found.group(2))))
            self.beacons.append((int(found.group(3)), int(found.group(4))))

    def count(self, y_: int) -> int:
        results = set()
        bx = set()
        
        for s,b in zip(self.sensors, self.beacons):
            d = distance(s,b)
            mxd = d - abs(s[1] - y_)
            if (mxd >= 0):
                for x in range(s[0] - mxd, s[0] + mxd + 1):
                    results.add(x)
            if (b[1] == y_):
                bx.add(b[0])
                
        return len(results - bx)
    
    def frequency(self, limit_: int) -> int:
        for y in range(limit_+1):
            ranges = []
            bx = set()
            for s,b in zip(self.sensors, self.beacons):
                d = distance(s,b)
                mxd = d - abs(s[1] - y)
                if (mxd >= 0):
                    ranges.append([s[0] - mxd, s[0] + mxd + 1])
                if (b[1] == y):
                    bx.add(b[0])
            
            ranges = sorted(ranges)
            x = getEmptyX(ranges, limit_)
            
            if (x > -1):
                return x * 4000000 + y
            
        return -1
    
    def run(self):
        self.load()
        
        if (TEST == 1):
            row = 10
            limit = 20
        else:
            row = 2000000
            limit = 4000000
        
        self.result1 = self.count(row)
        self.result2 = self.frequency(limit)
    
############################################################
# MAIN
############################################################
filename = "data/" + INPUT_FILES[TEST]
p = Puzzle(filename)
p.run()
print("Result 1: " + str(p.getResult1()))
print("Result 2: " + str(p.getResult2()))              
