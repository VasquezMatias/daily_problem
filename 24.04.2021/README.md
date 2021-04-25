# DAILY CODING PROBLEM #4 - 24/04/2021 [HARD]
* * *
Todays daily coding problem was asked by Stripe

## PRODUCT ARRAY EXCEPT i

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.


## My solution (python):

I went with a solution with sorting first, because it is `O(n log(n))`. If I went with something like the second solution, we get a complexity of `O(n²)` which is worse. This is because the built in function for searching (`in`) has a complexity of `O(n)` which is inside a for loop that iterates through every object in the list (also with complexity `O(n)`).

```python
def first_missing_positive(vals: list):
	vals.sort()
	i = 1
	for val in vals:
		if val < i:
			continue
		elif val == i:
			i += 1
		else:
			break
	return i


if __name__ == '__main__':
	print(first_missing_positive([3, 4, -1, 1]))
	print(first_missing_positive([1, 2, 0]))
```


## Worse solution (python):

```python
def first_missing_positive_bad(vals: list):
	for i in range(1, len(vals)):
		if not(i in vals):
			return i
	return i+1


if __name__ == '__main__':
	print(first_missing_positive_bad([3, 4, -1, 1]))
	print(first_missing_positive_bad([1, 2, 0]))

```