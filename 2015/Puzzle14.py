############################################################
# Import
############################################################
from Utils import *
from typing import List

############################################################
# Static Methods
############################################################
def computeDistance(data: List, time: int) -> List[int]:
    distance = [0 for i in range(len(data))]
    
    for i in range(len(data)):
        tFrame = data[i][1] + data[i][2]
        nFrame = time // tFrame
        distance[i] = nFrame * data[i][0] * data[i][1]
        
        tRemain = time - nFrame * tFrame
        distance[i] += data[i][0] * min(tRemain, data[i][1])
    
    return distance

############################################################
# Class Puzzle14
############################################################
class Puzzle14:
    def __init__(self, filename_: str):
        self.filename = filename_
        self.result1 = 0
        self.result2 = 0
    
    def getResult1(self) -> int:
        return self.result1

    def getResult2(self) -> int:
        return self.result2

    def run(self):
        time = 2503
        lines = readLines(self.filename)
        
        data = []
        for line in lines:
            found = re.fullmatch("(.+) can fly (.+) km/s for (.+) seconds, but then must rest for (.+) seconds.", line)
            data.append([int(found.group(2)), int(found.group(3)), int(found.group(4))])

        # Part 1
        distance = computeDistance(data, time)
        self.result1 = max(distance)
        
        # Part 2
        points = [0 for i in range(len(data))]
        for t in range(1, time):
            distance = computeDistance(data, t)

            for i in range(len(data)):
                if (distance[i] == max(distance)):
                    points[i] += 1
                    
        self.result2 = max(points)
        
        return            
