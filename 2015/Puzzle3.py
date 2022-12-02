############################################################
# Import
############################################################
from Utils import *

############################################################
# Class Puzzle3
############################################################
class Puzzle3:
    def __init__(self, filename_):
        self.filename = filename_
        self.result1 = 0
        self.result2 = 0
    
    def getResult1(self):
        return self.result1

    def getResult2(self):
        return self.result2
    
    def track(self, text, start = 0, step = 1):
        result = [[0, 0]]        
        x = 0
        y = 0
        
        for i in range(start, len(text), step):
            if (text[i] == 'v'):
                y -= 1
            elif (text[i] == '^'):
                y += 1
            elif (text[i] == '<'):
                x -= 1
            else:
                x += 1
            result.append([x, y])
        
        return result

    def run(self):
        text = readFile(self.filename)
        
        # Part 1
        points = self.track(text)
        points = [points[i] for i in range(len(points)) if i == points.index(points[i])]
        self.result1 = len(points)
        
        # Part 2
        santa = self.track(text, 0, 2)
        robot = self.track(text, 1, 2)
        points = santa + robot
        points = [points[i] for i in range(len(points)) if i == points.index(points[i])]
        self.result2 = len(points)
        
    
        return            
