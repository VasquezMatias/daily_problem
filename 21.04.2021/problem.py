
def add_up_to_k(l_o_n: list, k: int):
	for l in l_o_n:
		if k-l in l_o_n:
			return True
	return False

if __name__ == '__main__':
	list_of_numbers = [10, 15, 3, 7]
	tests = [17, -1, 5, 14, 28, 12.5]
	for k in tests:
		print(f"{k} -> {add_up_to_k(list_of_numbers, k)}")
