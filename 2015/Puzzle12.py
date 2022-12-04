############################################################
# Import
############################################################
from Utils import *

############################################################
# Class Puzzle12
############################################################
class Puzzle12:
    def __init__(self, filename_):
        self.filename = filename_
        self.result1 = 0
        self.result2 = 0
    
    def getResult1(self):
        return self.result1

    def getResult2(self):
        return self.result2

    def run(self):
        text = readFile(self.filename)        

        # Part 1
        tokens = apply(int, re.findall("-?\d+", text))        
        self.result1 = sum(tokens)
        
        # Part 
        tokens = re.split("[\"]", text)
        
        # for i in range(len(tokens)):
        #     if "red" in tokens[i]:
                
        
        
        return            
