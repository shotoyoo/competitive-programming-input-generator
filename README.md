# competitive-programming-input-generator

Auto-generator of random input for competitive programming using Python.

## Supported Macro

* Int(name,low,high)
* Float(name,low,high,number_of_digits)
* Array(Int(name,low,high),num)
* Perm(low,high): permutation of low, low+1, ..., high
* Str(*regular pattern*)
* Graph0(n,m): edges of unweighted 0_indexed connected graph
* Graph1(n,m): edges of unweighted 1_indexed connected graph (==Graph(n,m))
* Graph(n,m,low,high): edges of weighted graph with random weight w s.t. low<=w<=high
* Tree0(n): edges of unweighted 0_indexed graph
* Tree1(n): edges of unweighted 1_indexed graph (==Tree(n))
* Tree(n,low,high): edges of weighted tree with random weight w s.t. low<=w<=high

* "*N(v)" style ← repeat v preceeding rows N times (N can be a specific integer or a name of integer defined already)

(note that all values are specified in inclusive manner.)

## Environments

Required Python Libraries: 

* numpy
* rstr
* networkx
* pyperclip(optional)

Tested under Python 3.7.6


## Usage Example


```python
s = """Int(N,2,5)
Float(a,1,100,5) Perm(1,N+4)
Str([a-z]{3,2*N})
*N(2)
"""
lc = LineCollection.from_str(s)
print(lc.generate())

# output: 
# 4
# 54.81887 3 2 4 7 1 8 5 6
# yyl
# 4.32497 4 1 6 5 3 8 7 2
# yziuqiac
# 42.84603 3 2 4 7 8 6 5 1
# vsjajs
# 65.07176 7 5 8 3 4 6 1 2
# rbq
```

```python
s = """Int(N,10,20)
Array(Int(_,1,100),N)
"""
lc = LineCollection.from_str(s)
print(lc.generate())

# output:
# 19
# 64 52 27 31 5 8 2 18 82 65 92 51 61 98 73 64 55 56 94
```

```python
s = """Int(N,3,5) Int(M,N-1,N*(N-1)//2)
Graph1(N,M,0,1000)
"""
lc = LineCollection.from_str(s)
print(lc.generate())

# output:
# 4 5
# 1 2 392
# 1 3 328
# 1 4 891
# 2 3 264
# 3 4 227
```

```python
s = """Int(N,4,6) Int(M,4,6)
Str([.#]{M})
*N(1)
"""
lc = LineCollection.from_str(s)
print(lc.generate())

"""output:
4 5
###.#
#.#.#
#..##
.###.
"""
```


(This software is released under the MIT License)