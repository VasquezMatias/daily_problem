import numpy as np

def product_except_i(l: list):
    multiplication = np.prod(l)
    return [multiplication/i for i in l]

def product_except_i_no_div(l: list):
    return [np.prod(l[:i-1] + l[i:]) for i in range(1, len(l)+1)]


if __name__=='__main__':
    
    a = [1, 2, 3, 4, 5]
    b = [2, 4, 6, 8, 10]
    
    print(f"a = {a} -> {product_except_i(a)}")
    print(f"a = {a} -> {product_except_i_no_div(a)}")
    print(f"b = {b} -> {product_except_i(b)}")
    print(f"b = {b} -> {product_except_i_no_div(b)}")