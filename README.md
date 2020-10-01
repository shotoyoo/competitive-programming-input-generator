# competitive-programming-input-generator

under construction

Currently, these macros are supported: 

* Int(name,low,high)
* Float(name,low,high,number_of_digits)
* Perm(low,high)
* Str(*regular pattern*)
* Graph0(n,m): unweighted 0_indexed connected graph
* Graph1(n,m): unweighted 1_indexed connected graph (==Graph(n,m))
* Tree0(n): unweighted 0_indexed graph
* Tree1(n): unweighted 1_indexed graph (==Tree(n))
* (Graph|Tree)(n,m,low,high): weighted (graph|tree) with random weight w s.t. low<=w<=high

* "*N(v)" style ← repeat v rows N times (N can be a specific integer or a name of integer defined already)

(note that all values are specified in inclusive manner.)

## Required Python Libraries

numpy
rstr
networkx

## Usage Example

```python
s = """Int(N,2,5)
Float(a,1,100,5) Perm(1,N+4)
Str([a-z]{3,2*N})
*N(2)
"""
lc = generate.LineCollection.from_str(s)
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
rbq
```

```python
s = """Int(N,5,10) Int(M,N-1,N*(N-1)//2)
Graph1(N)
"""
    lc = LineCollection.from_str(s)
    print(lc.generate())

# output:
# 5 8
# 1 3 0
# 1 4 0
# 1 5 1
# 2 4 8
# 2 5 7
# 3 4 10
# 3 5 5
# 4 5 6
```