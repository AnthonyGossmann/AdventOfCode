############################################################
# IMPORT
############################################################
from Utils import *
import typing
from typing import Dict
from typing import List
from dataclasses import dataclass

############################################################
# CONFIGURATION
############################################################
TEST = 0

############################################################
# DEFINITIONS
############################################################
INPUT_FILES = ["07.txt", "07.ex"]

############################################################
# CLASS ITEM
############################################################
Item = typing.NewType("Item", None)
@dataclass()
class Item:
    parent: Item
    children: Dict[str, Item]
    size: int
    isDir: bool
    
############################################################
# METHODS
############################################################
        
############################################################
# CLASS PUZZLE
############################################################
class Puzzle:
    filename: str
    result1: int
    reuslt2: int
    root: Item
    
    def __init__(self, filename_: str):
        self.filename = filename_
        self.result1 = 0
        self.result2 = 1E9
        self.root = Item(None, {}, 0, True)
    
    def getResult1(self) -> int:
        return self.result1

    def getResult2(self) -> int:
        return self.result2
    
    def loadItems(self):
        lines = readLines(self.filename)
        
        current = self.root
        for line in lines:
            if line.startswith("$ cd"):
                name = line.replace("$ cd ", "")
                if (name == "/"):
                    current = self.root
                elif (name == ".."):
                    if (current != self.root):
                        current = current.parent
                else:
                    current = current.children[name]
            elif line.startswith("$ ls"):
                continue
            elif line.startswith("dir"):
                name = line.replace("dir ", "")
                current.children[name] = Item(current, {}, 0, True)
            else:
                [size, name] = re.split(" ", line)
                current.children[name] = Item(current, {}, int(size), False)
      
                it = current
                while True:
                    it.size += int(size)
                    if (it.parent == None):
                        break
                    it = it.parent

    def getDirs(self, src_: Item) -> List:
        items = []
        for item in src_.children.values():
            if (item.isDir and (item != self.root)):
                items.append(item)
                items += self.getDirs(item)
        return items
                  
    def run(self):
        self.loadItems()
        items = self.getDirs(self.root)
            
        # Part 1
        for item in items:
            if (item.size <= 100000):
                self.result1 += item.size

        # Part 2
        target = 30000000 - (70000000 - self.root.size)
        for item in items:
            if (item.size >= target):
                if (item.size < self.result2):
                    self.result2 = item.size    
                    
############################################################
# MAIN
############################################################
filename = "data/" + INPUT_FILES[TEST]
p = Puzzle(filename)
p.run()
print("Result 1: " + str(p.getResult1()))
print("Result 2: " + str(p.getResult2()))
