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

def first_missing_positive_bad(vals: list):
	for i in range(1, len(vals)):
		if not(i in vals):
			return i
	return i+1


if __name__ == '__main__':
	print(first_missing_positive([3, 4, -1, 1]))
	print(first_missing_positive([1, 2, 0]))

	print(first_missing_positive_bad([3, 4, -1, 1]))
	print(first_missing_positive_bad([1, 2, 0]))
