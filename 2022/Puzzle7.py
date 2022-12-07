############################################################
# Import
############################################################
from Utils import *
from typing import List

############################################################
# Static Methods
############################################################
def buildKey(name_: str, parent_: str) -> str:
    if (name_ == "/"):
        return None
    elif (parent_ == "/"):
        return parent_ + name_
    else:
        return parent_ + "/" + name_
    
############################################################
# Class Item
############################################################
class Item:
    def __init__(self, name_: str, parent_ = None, isDir_: bool = True, size_: int = 0):
        self.name = name_
        self.parent = parent_
        self.isDir = isDir_
        self.size = size_
        self.children = []
        
        if (name_ == "/"):
            self.key = name_
        elif (parent_ == "/"):
            self.key = parent_ + name_
        else:
            self.key = parent_ + "/" + name_
        
############################################################
# Class Puzzle7
############################################################
class Puzzle7:
    def __init__(self, filename_: str):
        self.filename = filename_
        self.result1 = 0
        self.result2 = 1E9
        self.items = {}
    
    def getResult1(self) -> int:
        return self.result1

    def getResult2(self) -> int:
        return self.result2
    
    def getTargetDirectory(self, name_: str, current_: str, currentParent_: str):
        if (name_ == ".."):
            if (current_ != "/"):
                return self.items[currentParent_]
        elif (name_ == "/"):
            return self.items["/"]
        else:
            return self.items[buildKey(name_, current_)]
    
    def loadItems(self, lines_: List[str]):
        item = Item("/", None, True)
        self.items[item.key] = item
        
        current = self.items["/"]
        for line in lines_:
            if line.startswith("$ cd"):
                # cd
                token = line.replace("$ cd ", "")
                current = self.getTargetDirectory(token, current.key, current.parent)
            elif line.startswith("$ ls"):
                # ls
                continue
            elif line.startswith("dir"):
                # Dir
                token = line.replace("dir ", "")
                item = Item(token, current.key, True)
                if (item.key not in self.items.keys()):
                    self.items[item.key] = item
                current.children.append(item.key)
            else:
                # File
                tokens = re.split(" ", line)
                item = Item(tokens[1], current.key, False, int(tokens[0]))
                if (item.key not in self.items.keys()):
                    self.items[item.key] = item
                current.children.append(item.key)
                
                # Update parent size
                it = current
                while True:
                    it.size += self.items[item.key].size
                    if (it.parent == None):
                        break
                    it = self.items[it.parent]

    def run(self):
        lines = readLines(self.filename)
        self.loadItems(lines)
            
        # Part 1
        for item in self.items.values():
            if (item.key == "/"):
                continue
            if (item.isDir and (item.size <= 100000)):
                self.result1 += item.size

        # Part 2
        total = 70000000
        target = 30000000
        free = total - self.items["/"].size
        need = target - free
        
        for item in self.items.values():
            if (item.key == "/"):
                continue
            if not item.isDir:
                continue
            if (item.size >= need):
                if (item.size < self.result2):
                    self.result2 = item.size            
    
        return            
