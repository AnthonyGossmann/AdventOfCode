############################################################
# Import
############################################################
from Utils import *
import typing
from typing import Dict
from dataclasses import dataclass

Item = typing.NewType("Item", None)
    
############################################################
# Class Item
############################################################
@dataclass()
class Item:
    parent: Item
    children: Dict[str, Item]
    size: int
    isDir: bool
        
############################################################
# Class Puzzle7
############################################################
class Puzzle7:
    def __init__(self, filename_: str):
        self.filename = filename_
        self.result1 = 0
        self.result2 = 1E9
    
    def getResult1(self) -> int:
        return self.result1

    def getResult2(self) -> int:
        return self.result2
    
    def loadItems(self, lines_: List[str]) -> Item:
        root = Item(None, {}, 0, True)
        
        current = root
        for line in lines_:
            if line.startswith("$ cd"):
                name = line.replace("$ cd ", "")
                if (name == "/"):
                    current = root
                elif (name == ".."):
                    if (current != root):
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
                    
        return root

    def getDirs(self, root_: Item) -> List[Item]:
        items = []
        for item in root_.children.values():
            if item.isDir:
                items.append(item)
                items += self.getDirs(item)
        return items
                
                
    def run(self):
        lines = readLines(self.filename)
        root = self.loadItems(lines)
            
        # Part 1
        items = self.getDirs(root)
        for item in items:
            if ((item != root) and (item.size <= 100000)):
                self.result1 += item.size

        # Part 2
        target = 30000000 - (70000000 - root.size)
        for item in items:
            if ((item != root) and (item.size >= target)):
                if (item.size < self.result2):
                    self.result2 = item.size    
    
        return            
