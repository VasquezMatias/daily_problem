# Daily Problem 16/10/2022

class Collatz():
    def test(self, x):
        iter = 0
        while x > 1:
            iter += 1

            if x % 2 == 0:
                x = x / 2
            else:
                x = 3 * x + 1
        return x==1, iter

    def logest_seq(self, x):
        highest = 0
        for i in range(x//2, x):
            _, iter = self.test(i)
            if iter > highest:
                highest = iter
                highest_n = i

        return highest_n, highest

    
col = Collatz()

print(col.test(30))
print(col.test(1_000_000))
print(col.logest_seq(1_000_000))
