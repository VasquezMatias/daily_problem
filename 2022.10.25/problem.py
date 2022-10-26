

class Smaller():
    def smaller(self, arr) -> list:
        small = [0] * len(arr)
        for i, elem in enumerate(arr):
            for rest in arr[i:]:
                if rest<elem:
                    small[i] += 1
        
        return small

arr = [3, 4, 9, 6, 1]
s = Smaller()
print(s.smaller(arr))