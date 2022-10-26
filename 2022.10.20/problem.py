
class RunLength():
    def encode(self, s) -> str:
        n = 0
        last = ""
        enc = ""
        l = len(s)
        for i, letter in enumerate(s):
            if letter == last:
                n += 1
                if i==l-1:
                    enc += str(n) + last
            else:
                if n>0:
                    enc += str(n) + last
                n = 1
                last = letter

        return enc
    
    def decode(self, s) -> str:
        dec = ""
        for i, letter in enumerate(s):
            if i%2==0:
                n = int(letter)
            else:
                dec += letter * n

        return dec



enc = "AAAABBBCCDAA"
dec = "4A3B2C1D2A"

rl = RunLength()
print(rl.encode(enc))
print(rl.decode(dec))