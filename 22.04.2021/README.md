# DAILY CODING PROBLEM #2 - 22/04/2021 [HARD]
* * *
Todays daily coding problem was asked by Uber

## PRODUCT ARRAY EXCEPT i

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

```python
import numpy as np

def product_except_i(l: list):
    multiplication = np.prod(l)
    return [multiplication/i for i in l]

if __name__=='__main__':
    
    a = [1, 2, 3, 4, 5]
    b = [2, 4, 6, 8, 10]
    
    print(f"a = {a} -> {product_except_i(a)}")
    print(f"b = {b} -> {product_except_i(b)}")
```

Follow-up: what if you can't use division?

```python
import numpy as np

def product_except_i_no_div(l: list):
    return [np.prod(l[:i-1] + l[i:]) for i in range(1, len(l)+1)]


if __name__=='__main__':
    
    a = [1, 2, 3, 4, 5]
    b = [2, 4, 6, 8, 10]
    
    print(f"a = {a} -> {product_except_i_no_div(a)}")
    print(f"b = {b} -> {product_except_i_no_div(b)}")
```

