
def n_decoding_ways(code: int):
	code = str(code)
	j = 1
	for i, letter in enumerate(code):
		print(f"{i} - {letter}")
		if(i < len(code)-1):
			if(letter=='1' and code[i+1] != '0'):
				j+=1
			if(letter=='2' and code[i+1] != '0' and int(code[i+1]) < 7):
				j+=1
	return j

if __name__ == '__main__':
	print(n_decoding_ways(111126))
