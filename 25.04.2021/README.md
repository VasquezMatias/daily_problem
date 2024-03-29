# DAILY CODING PROBLEM #5 - 25/04/2021 [HARD]
* * *
Todays daily coding problem was asked by Jane Street

## PAIR CONSTRUCTION -> FIRST/LAST ELEMENT

`cons(a, b)` constructs a pair, and `car(pair)` and `cdr(pair)` returns the first and last element of that pair. For example, `car(cons(3, 4))` returns 3, and `cdr(cons(3, 4))` returns 4.

Given this implementation of cons:
```python
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
```
Implement car and cdr.

## My solution (python):


```python
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

def car(pair):
	def first(a, b):
		return a
	return pair(first)

def cdr(pair):
	def last(a,b):
		return b
	return pair(last)


if __name__ == '__main__':
	print(car(cons(3, 4)))
	print(cdr(cons(3, 4)))
```
