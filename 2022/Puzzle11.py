############################################################
# IMPORT
############################################################
from Utils import *
from itertools import product
import typing
from typing import NewType
from typing import Dict
from typing import List
from dataclasses import dataclass
import re

############################################################
# CONFIGURATION
############################################################
TEST = 0

############################################################
# DEFINITIONS
############################################################
INPUT_FILES = ["11.txt", "11.ex"]

############################################################
# CLASS MONKEY
############################################################
Monkey = typing.NewType("Monkey", None)
class Monkey:
    name: int
    items: List[int]
    op: str
    test: int
    dst0: int
    dst1: int
    ctr: int

    def __init__(self, name_: int, items_: List[int], op_: str, test_: int, dst0_: int, dst1_: int):
        self.name = name_
        self.items = items_
        self.op = op_
        self.test = test_
        self.dst0 = dst0_
        self.dst1 = dst1_
        self.ctr = 0
        
    def worry(self, old_: int) -> int:
        tokens = re.split(' ', self.op)
        if (tokens[0] == '+'):
            return old_ + int(tokens[1])
        elif (tokens[1] == 'old'):
            return old_ * old_
        else:
            return old_ * int(tokens[1])
        
    def inspect(self, monkeys_: Dict[int,Monkey], mod_: int = 3):
        for item in self.items:
            self.ctr += 1
            w = self.worry(item)
            
            if (mod_ == 3):
                w = w // mod_
            else:
                w = w % mod_
                
            if ((w % self.test) == 0):
                monkeys_[self.dst1].items.append(w)
            else:
                monkeys_[self.dst0].items.append(w)
                
        self.items.clear()
    
############################################################
# METHODS
############################################################

############################################################
# CLASS PUZZLE
############################################################
class Puzzle:
    filename: str
    result1: int
    result2: int
    monkeys: Dict[int,Monkey]
    
    def __init__(self, filename_: str):
        self.filename = filename_
        self.result1 = 0
        self.result2 = 0
    
    def getResult1(self) -> int:
        return self.result1

    def getResult2(self) -> int:
        return self.result2
    
    def load(self):
        self.monkeys = {}
        text = readFile(self.filename)
        text = text.replace('\n', ',')
        lines = text.split(',,')
        
        for line in lines:
            line = ' '.join(list(filter(None, re.split(' ', line)))).rstrip(',')
            found = re.fullmatch("Monkey (.+):, Starting items: (.+), Operation: new = old (.+), Test: divisible by (.+), If true: throw to monkey (.+), If false: throw to monkey (.+)", line)
            items = apply(int, re.split(',', found.group(2)))
            self.monkeys[int(found.group(1))] = Monkey(int(found.group(1)), items, found.group(3), int(found.group(4)), int(found.group(6)), int(found.group(5)))
        
    def run(self):
        # Part 1
        self.load()
        for i,j in product(range(20), range(len(self.monkeys))):
            self.monkeys[j].inspect(self.monkeys)
            
        ctr = [m.ctr for m in self.monkeys.values()]
        ctr.sort()
        self.result1 = ctr[-1] * ctr[-2]
        
        # Part 2
        self.load()
        mod = 1
        for m in self.monkeys.values():
            mod *= m.test
            
        for i,j in product(range(10000), range(len(self.monkeys))):
            self.monkeys[j].inspect(self.monkeys, mod)
            
        ctr = [m.ctr for m in self.monkeys.values()]
        ctr.sort()
        self.result2 = ctr[-1] * ctr[-2]

############################################################
# MAIN
############################################################
filename = "data/" + INPUT_FILES[TEST]
p = Puzzle(filename)
p.run()
print("Result 1: " + str(p.getResult1()))
print("Result 2: " + str(p.getResult2()))