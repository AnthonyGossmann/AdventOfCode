############################################################
# Import
############################################################
from Utils import *

############################################################
# Class Puzzle16
############################################################
class Puzzle16:
    filename: str
    result1: int
    result2: int
    
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
        
        data = dict()
        for line in lines:
            found = re.fullmatch("Sue (.+): (.+): (.+), (.+): (.+), (.+): (.+)", line)
            for i in range(2, 7, 2):
                data.setdefault(int(found.group(1)), dict())[found.group(i)] = int(found.group(i+1))
                
        ticker = {
            "children"   : 3,
            "cats"       : 7,
            "samoyeds"   : 2,
            "pomeranians": 3,
            "akitas"     : 0,
            "vizslas"    : 0,
            "goldfish"   : 5,
            "trees"      : 3,
            "cars"       : 2,
            "perfumes"   : 1 }
        
        # Part 1
        for key in data.keys():
            match = True
            for tkey in ticker.keys():
                if ((tkey in data[key].keys()) and (ticker[tkey] != data[key][tkey])):
                    match = False
            if match:
                self.result1 = key
                break

        # Part 2
        for key in data.keys():
            match = True
            for tkey in ticker.keys():
                if (tkey in data[key].keys()):
                    if ((tkey == "cats") or (tkey == "trees")):
                        if (ticker[tkey] >= data[key][tkey]):
                            match = False
                    elif ((tkey == "pomeranians") or (tkey == "goldfish")):
                        if (ticker[tkey] <= data[key][tkey]):
                            match = False
                    else:
                        if (ticker[tkey] != data[key][tkey]):
                            match = False
                        
            if match:
                self.result2 = key
                break

        return            
