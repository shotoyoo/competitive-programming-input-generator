# competitive-programming-input-generator

under construction

Currently, these macros are supported: 

* Int(name,low,high)
* Float(name,low,high,number_of_digits)
* Perm(low,high)
* Str(*regular pattern*)
* "*N(v)" style ← repeat v rows N times (N can be a specific integer or a name of integer defined already)

(note that all values are specified in inclusive manner.)

## Required Python Libraries

numpy
rstr

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
4
54.81887 3 2 4 7 1 8 5 6
yyl
4.32497 4 1 6 5 3 8 7 2
yziuqiac
42.84603 3 2 4 7 8 6 5 1
vsjajs
65.07176 7 5 8 3 4 6 1 2
rbq```
