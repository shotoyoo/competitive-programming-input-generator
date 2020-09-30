# competitive-programming-input-generator

under construction

Currently, these macros below are supported: 

* Int(name,low,high)
* Float(name,low,high,number_of_digits)
* Perm(low,high)
* "*N(v)" style ← repeat v rows N times (N can be a specific integer or a name of integer defined already)

(note that all values are specified in inclusive manner.)

## Usage

```python
s = """Int(N,2,10)
Float(a,1,100,5) Perm(1,N)
*N(1)
"""
lc = generate.LineCollection.from_str(s)
print(lc.generate())

# output: 
10
94.26919 10 7 2 6 4 8 9 1 5 3
50.48968 4 10 7 3 9 5 2 6 1 8
76.01515 4 6 5 8 1 10 9 7 2 3
93.27390 2 10 5 9 8 3 6 7 4 1
98.13830 6 7 2 9 5 3 10 1 4 8
48.51880 9 7 3 2 5 6 10 4 8 1
3.80817 8 1 2 5 3 7 9 6 10 4
84.29041 5 2 1 9 8 10 6 3 4 7
24.92589 6 2 3 8 4 10 5 9 1 7
81.16136 2 8 9 7 3 1 5 4 6 10
95.94868 3 1 10 8 5 4 6 2 9 7
```
