# DAILY CODING PROBLEM #1 - 21/04/2021 [EASY]
* * *
Todays daily coding problem was asked by Google

## SUM OF TWO VALUES

Given a list of numbers and a number k, return whether any two numbers from the list add up to k.

For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

Bonus: Can you do this in one pass?



```python
def add_to_k(l_o_n: list, k: int):
	for l in l_o_n:
		if k-l in l_o_n:
			return True
	return False

if __name__ == '__main__':
	list_of_numbers = [10, 15, 3, 7]
	tests = [17, -1, 5, 14, 28, 12.5]
	for k in tests:
		print(f"{k} -> {add_to_k(list_of_numbers, k)}")
```