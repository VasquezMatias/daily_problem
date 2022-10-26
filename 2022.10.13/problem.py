

class Palindrome():
    def palindrome(self, word) -> bool:
        abc = dict()

        for letter in word:
            if letter in abc:
                abc[letter] += 1
            else:
                abc[letter] = 1

        singles = 0
        for key in abc:
            if abc[key] % 2 != 0:
                singles += 1
            if singles > 1:
                return False

        return True


w1 = "carrace"
w2 = "daily"

pal = Palindrome()
print(pal.palindrome(w1))
print(pal.palindrome(w2))