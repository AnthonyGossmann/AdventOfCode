############################################################
# Import
############################################################
from Utils import *
from itertools import product
import typing
from typing import Dict
from typing import List
from typing import NewType
from dataclasses import dataclass
import re

############################################################
# Class Monkey
############################################################
Monkey = typing.NewType("Monkey", None)
@dataclass()
class Monkey:
    name: int
    items: List[int]
    operation: str
    divider: int
    dst0: int
    dst1: int
    counter: int
    
    def __init__(self, name_: int, items_: List[int], operation_: str, divider_: int, dst0_: int, dst1_: int):
        self.name = name_
        self.items = items_
        self.operation = operation_
        self.divider = divider_
        self.dst0 = dst0_
        self.dst1 = dst1_
        self.counter = 0
        
    def worry(self, old_: int) -> int:
        tokens = re.split(" ", self.operation)
        if (tokens[0] == '+'):
            return old_ + int(tokens[1])
        elif (tokens[1] == 'old'):
            return old_ * old_
        else:
            return old_ * int(tokens[1])
        
    def inspect(self, monkeys_: List[Monkey], mod_: int = 0):
        for item in self.items:
            self.counter += 1
            w = self.worry(item)
            
            if (mod_ == 0):
                w = w // 3
            else:
                w = w % mod_
            
            if ((w % self.divider) == 0):
                monkeys_[self.dst1].items.append(w)
            else:
                monkeys_[self.dst0].items.append(w)
        self.items.clear()

############################################################
# Class Puzzle11
############################################################
class Puzzle11:
    filename: str
    result1: int
    result2: int
    
    def __init__(self, filename_):
        self.filename = filename_
        self.result1 = 0
        self.result2 = 0
    
    def getResult1(self):
        return self.result1

    def getResult2(self):
        return self.result2
    
    def load(self, text_: str) -> Dict[int,Monkey]:
        monkeys = {}
        text = text_.replace('\n', ',')
        lines = text.split(',,')
        
        for line in lines:
            line = " ".join(list(filter(None, re.split(" ", line)))).rstrip(",")
            found = re.fullmatch("Monkey (.+):, Starting items: (.+), Operation: new = old (.+), Test: divisible by (.+), If true: throw to monkey (.+), If false: throw to monkey (.+)", line)     
            items = apply(int, re.split(',', found.group(2)))
            monkeys[int(found.group(1))] = Monkey(int(found.group(1)), items, found.group(3), int(found.group(4)), int(found.group(6)), int(found.group(5)))
        
        return monkeys

    def run(self):
        text = readFile(self.filename)
        
        # Part 1
        monkeys = self.load(text)
        for i,j in product(range(20), range(len(monkeys))):
            monkeys[j].inspect(monkeys)
                
        ctr = [m.counter for m in monkeys.values()]
        ctr.sort()
        self.result1 = ctr[-1] * ctr[-2]
        
        # Part 2
        monkeys.clear()
        monkeys = self.load(text)

        mod = 1
        for m in monkeys.values():
            mod *= m.divider
            
        for i,j in product(range(10000), range(len(monkeys))):
            monkeys[j].inspect(monkeys, mod)
                
        ctr = [m.counter for m in monkeys.values()]
        ctr.sort()
        self.result2 = ctr[-1] * ctr[-2]
    
        return            
