import os
import sys
sys.path.append(os.path.dirname(__file__))
import pdb
import rstr
import utils
from items import *
from graph import *

def evaluate_item(ss):
    cc, tmp = ss.split("(", 1)
    vv = tmp[:-1]
    return globals()[cc].from_str(vv)

class Array(Item):
    def __init__(self, item, num):
        self.item = item
        self.num = num
    @classmethod
    def from_str(cls, s):
        item,num = s.rsplit(",", 1)
        return cls(evaluate_item(item), num)
    def generate(self):
        return " ".join(map(str, [self.item.generate() for _ in range(self.evaluate(self.num))]))

class Line:
    def __init__(self, l, s=None):
        """
        correspond to a line of input file
        l: list of Item
        """
        self.l = l
        self.s = s
    @classmethod
    def from_str(cls, s):
        l = []
        for ss in s.split():
            l.append(evaluate_item(ss))
        return cls(l)
    def generate(self):
        return " ".join([item.generate() for item in self.l])

class LineCollection:
    def __init__(self, ls, s=None):
        """ls: list of Line
        """
        self.ls = ls
        self.s = s
    @classmethod
    def from_str(cls, s):
        lines = s.split("\n")
        i = 0
        ls = []
        for i in range(len(lines)):
            if lines[i].startswith("*"):
                name, num = lines[i][1:].split("(",1)
                num = int(num[:-1])
                ls.append((name, num))
            else:
                l = Line.from_str(lines[i])
                ls.append(l)
        return cls(ls, s)
    def generate(self):
        i = 0
        prv = 0
        output = []
        while i<len(self.ls):
            while i<len(self.ls) and not isinstance(self.ls[i], tuple):
                i += 1
            if i<len(self.ls) and isinstance(self.ls[i], tuple):
                m, num = self.ls[i]
                i += 1
            else:
                m = 0
                num = 0
            for j in range(prv, i-num-1):
                if isinstance(self.ls[j], tuple):
                    continue
                output.append(self.ls[j].generate())
            if num!=0:
                try:
                    m = Item.names[m]
                except KeyError:
                    raise ValueError("テストケース数が未定義: 上何行見るかの指定が間違っていません？")
                for _ in range(m):
                    for j in range(i-num-1, i-1):
                        if isinstance(self.ls[j], tuple):
                            continue
                        output.append(self.ls[j].generate())
            prv = i
        return "\n".join(output)

if __name__=="__main__":
    s = """Int(T,2,10)
Int(N,1,10)
Perm(2,N+5)
*T(2)
"""
    s = """Int(N,3,5) Int(M,N-1,N*(N-1)//2)
Graph1(N,M,0,10)
"""
    s = """Int(N,10,20)
Array(Int(_,1,100),N)
    """
    lc = LineCollection.from_str(s)
    print(lc.generate())

    # import pyperclip
    # lc = LineCollection.from_str(s)
    # print(lc.generate())
    # pyperclip.copy(lc.generate()) # copy to clipboard
