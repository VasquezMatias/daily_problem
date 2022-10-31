

from tkinter import E


class Unique():
    def single(self, array): 
        ones, twos = 0, 0 
        for x in array: 
            ones, twos = (ones ^ x) & ~twos, (ones & x) | (twos & ~x) 
        assert twos == 0 
        return ones 


unique = Unique()
l = [6, 1, 3, 3, 3, 6, 6]

print(unique.single(l))

l = [13, 19, 13, 13]
print(unique.single(l))

l = [1, 2, 3, 1, 2, 3, 4, 1, 2, 3]
print(unique.single(l))