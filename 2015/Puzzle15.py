############################################################
# Import
############################################################
from Utils import *
from itertools import product

############################################################
# Class Puzzle15
############################################################
class Puzzle15:
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
        
        data = []
        for line in lines:
            found = re.fullmatch("(.+): capacity (.+), durability (.+), flavor (.+), texture (.+), calories (.+)", line)
            data.append([int(found.group(2)), int(found.group(3)), int(found.group(4)), int(found.group(5)), int(found.group(6))])
        
        coefficients = [range(101) for i in data]
        for coeff in product(*coefficients):
            if (sum(coeff) != 100):
                continue

            properties = [0 for i in data[0]]
            for i in range(len(coeff)):
                for j in range(len(data[0])):
                    properties[j] += coeff[i] * data[i][j]
                
            properties = [0 if x < 0 else x for x in properties]
            score = properties[0] * properties[1] * properties[2] * properties[3]
            
            if (score > self.result1):
                self.result1 = score
                
            if ((properties[4] == 500) and (score > self.result2)):
                self.result2 = score
    
        return            
