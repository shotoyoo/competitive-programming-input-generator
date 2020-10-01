import pdb
import rstr
import utils

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
        value = utils.rng.integers(low, high+1)
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
        s = str(utils.rng.uniform(low, high))
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
        return " ".join(map(str, (utils.rng.permutation(high-low+1) + low).tolist()))
        
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
