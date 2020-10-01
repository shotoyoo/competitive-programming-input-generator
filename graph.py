import networkx as nx
import numpy as np

from items import *
import utils

def random_connected_graph(n,m):
    if m<=n*(n-1)//2 * 0.5:
        # sparse random graph
        # add edges to random tree
        g = nx.random_tree(n)
        l = list(range(n))
        num = 0
        while num<m-n+1:
            i,j = utils.rng.choice(l, 2)
            if (i,j) not in g.edges:
                num += 1
                g.add_edge(i,j)
    else:
        g = nx.complete_graph(n)
        l = list(range(n))
        num = 0
        to = n*(n-1)//2 - m
        while num<to:
            i,j = utils.rng.choice(l, 2)
            if (i,j) in g.edges:
                num += 1
                g.remove_edge(i,j)
    return g

class Graph(Item):
    """edge set of graph (n,m)
    if low&high specified, treated as weighted graph
    """
    index_by_0 = False
    def __init__(self, n, m, low=None, high=None):
        self.n = n
        self.m = m
        self.low = low
        self.high = high
    @classmethod
    def from_str(cls, s):
        v = s.split(",")
        if len(v)==2:
            n,m = v
            return cls(n,m)
        else:
            n,m,low,high = v
            return cls(n,m,low,high)
    def generate(self):
        n, m = self.evaluate(self.n), self.evaluate(self.m)
        g = random_connected_graph(n, m)
        output = []
        if self.low is not None:
            low, high = self.evaluate(self.low), self.evaluate(self.high)
            cs = utils.rng.integers(low, high+1, size=m)
            if self.index_by_0:
                for (i,j), c in zip(g.edges, cs):
                    output.append(" ".join(map(str, (i,j,c))))
            else:
                for (i,j), c in zip(g.edges, cs):
                    output.append(" ".join(map(str, (i+1,j+1,c))))
        else:
            if self.index_by_0:
                for i,j in g.edges:
                    output.append(" ".join(map(str, (i,j))))
            else:
                for i,j in g.edges:
                    output.append(" ".join(map(str, (i+1,j+1))))
        return "\n".join(output)

class Tree(Graph):
    @classmethod
    def from_str(cls, s):
        s = s.split(",")
        if len(s)==1:
            n = s[0]
            m = "%s-1" % n
            return Graph(n,m)
        else:
            n,low,high = s
            m = "%s-1" % n
            return Graph(n,m,low,high)

class Graph0(Graph):
    pass
class Graph1(Graph):
    index_by_0 = False
class Tree0(Tree):
    pass
class Tree1(Tree):
    index_by_0 = True
