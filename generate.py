import copy
import pdb

import rstr
import numpy as np

SEED = 0
rng = np.random.default_rng(SEED)

class Item:
    names = {}
    def __init__(self, s=None, **keys):
        self.s = s
    @classmethod
    def from_str(cls, s):
        pass
    def evaluate(self, s):
        for k in Item.names.keys():
            if k in s:
                s = s.replace(k, str(Item.names[k]))
        # if s in Item.names:
        #     return Item.names[s]
        return eval(s)
    def generate(self):
        pass
    def __str__(self):
        if hasattr(self, "s"):
            return self.s

class Int(Item):
    def __init__(self, name, low, high, s=None, **keys):
        """
        correspond to the input value between two spaces
        name: str
            name of variable
        low/high : str
            min / max (inclusive)
        """
        self.name = name
        self.low = low
        self.high = high
        self.keys = keys
        Item.__init__(self, s)
    @classmethod
    def from_str(cls, s):
        name, low, high = s.split(",")
        return cls(name, low, high, s=s)
    def generate(self):
        low, high = self.evaluate(self.low), self.evaluate(self.high)
        value = rng.integers(low, high+1)
        Item.names[self.name] = value
        return str(value)
    def __str__(self):
        if hasattr(self, "s"):
            return self.s

class Float(Int):
    """float value of [low, high) with digit numbers after decimal point
    """
    @classmethod
    def from_str(cls, s):
        name, low, high, digit = s.split(",")
        return cls(name, low, high, s=s, digit=digit)
    def generate(self):
        low, high = self.evaluate(self.low), self.evaluate(self.high)
        s = str(rng.uniform(low, high))
        sp = s.split(".")
        s = sp[0]+"."+sp[1][:int(self.keys["digit"])]
        Item.names[self.name] = float(s)
        return s

class Perm(Item):
    """permutation of [low, low+1, ..., high-1, high]
    """
    def __init__(self, low, high, s=None):
        self.low = low
        self.high = high
        self.s = s
    @classmethod
    def from_str(cls, s):
        low, high = s.split(",")
        return cls(low, high, s=s)
    def generate(self):
        low, high = self.evaluate(self.low), self.evaluate(self.high)
        return " ".join(map(str, (rng.permutation(high-low+1) + low).tolist()))
        
class Str(Item):
    def __init__(self, pattern):
        """
        pattern : str
            regular expression pattern
            s.t. 
            [a-zA-Z]{10}
            [a-z]{10,Name}
            (value of Name will be substituted runtime)
            You cannot specify complicated pattern which does not exist in above example
        """
        self.pattern = pattern
        self.s = pattern
    @classmethod
    def from_str(cls, s):
        return cls(s)
    def generate(self):
        pattern = self.pattern
        if "{" in pattern:
            p, tmp = pattern.split("{", 1)
            val, other = tmp.split("}", 1)
            l = []
            for item in val.split(","):
                l.append(str(self.evaluate(item)))
            pattern = p + "{" + ",".join(l) + "}" + other
        return rstr.xeger(pattern)
         
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
            cc, tmp = ss.split("(")
            vv = tmp[:-1]
            l.append(globals()[cc].from_str(vv))
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
        while i<len(lines):
            if i+1<len(lines) and lines[i+1].startswith("*"):
                l = Line.from_str(lines[i])
                ls.append(l)
                # *T(4) のような行のparse
                name, num = lines[i+1][1:].split("(",1)
                num = int(num[:-1])
                ls.append((name, num))
                i += 2
            else:
                l = Line.from_str(lines[i])
                ls.append(l)
                i += 1
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
            for j in range(prv, i-num):
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
    s = """Int(N,2,10)
Float(a,1,100,5) Str([a-z]{N,2*N})
*N(1)
"""
    lc = LineCollection.from_str(s)
    print(lc.generate())
